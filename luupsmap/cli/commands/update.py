import csv
from tempfile import NamedTemporaryFile

import googlemaps

from luupsmap.cli.csv_helper import strip_whitepace, pretty_file
from luupsmap import app

LINE_LENGTH = 25


class UpdateCommand:
    LOCATION_FIELDNAMES = ['name', 'address', 'latitude', 'longitude']
    VENUES_FIELDNAMES = ['name', 'homepage', 'email', 'phone', 'opening_hours', 'description']

    locations = {}
    places = {}
    venues = []

    def __init__(self, locations_file, venues_file):
        self.locations_file = locations_file
        self.venues_file = venues_file

    def run(self):
        self._load_venues_file()
        self._load_locations_file()
        self._update_venues()
        self._update_locations()
        self._create_locations()
        self._write_venues()
        self._write_locations()

    def _load_venues_file(self):
        print('Loading venues file...'.ljust(LINE_LENGTH), end=' ')
        processed_venues_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.venues_file, processed_venues_file)
        with open(processed_venues_file.name, 'r') as infile:
            reader = csv.DictReader(infile, fieldnames=self.VENUES_FIELDNAMES, delimiter='|')
            next(reader, None)
            for row in reader:
                self.venues.append(row)
        print('Done')

    def _load_locations_file(self):
        print('Loading address file...'.ljust(LINE_LENGTH), end=' ')
        processed_address_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.locations_file, processed_address_file)
        with open(processed_address_file.name, 'r') as infile:
            reader = csv.DictReader(infile, fieldnames=self.LOCATION_FIELDNAMES, delimiter='|')
            next(reader, None)
            for row in reader:
                key = row['name']
                if key in self.locations:
                    self.locations[key].append(row)
                else:
                    self.locations[key] = [row]

        print('Done')

    def _update_venues(self):
        print('Updating venues...'.ljust(LINE_LENGTH))
        for venue in self.venues:
            empty_fields = self._empty_fields(venue)
            if not empty_fields:
                continue
            if 'homepage' in empty_fields or 'phone' in empty_fields:
                self._update_venue(venue)
        print('Done')

    def _update_venue(self, venue):
        name = venue['name']
        place_details = self._get_place_details(name)
        if not place_details:
            return
        # TODO: Currently only first place is used, change when data moves to locations
        place_details = place_details[0]
        if 'website' in place_details and venue['homepage'] in (None, ''):
            venue['homepage'] = place_details['website']
            print('    {:<40s}{:<30s}'.format(name, place_details['website']))
        if 'international_phone_number' in place_details and venue['phone'] in (None, ''):
            venue['phone'] = place_details['international_phone_number']
            print('    {:<40s}{:<30s}'.format(name, place_details['international_phone_number']))

    @staticmethod
    def _empty_fields(dictionary):
        missing = []
        for k, v in dictionary.items():
            if dictionary[k] in (None, ''):
                missing.append(k)
        return missing

    def _update_locations(self):
        print('Updating locations...'.ljust(LINE_LENGTH))
        # TODO: Flatten nested locations for great profit
        for key, locations in self.locations.items():
            for location in locations:
                coordinates_missing = location['latitude'] in (None, '') or location['longitude'] in (None, '')
                if not coordinates_missing:
                    continue
                name = location['name']
                address = location['address']
                # TODO: Use existing place details data to avoid another call to google api
                [latitude, longitude] = self._fetch_location(address)
                location['latitude'] = latitude
                location['longitude'] = longitude
                print('    {:<40s}{:<60s}{:>12.1f}{:>12.1f}'.format(name, address, latitude, longitude))

    def _create_locations(self):
        print('Fetching new locations...'.ljust(LINE_LENGTH))
        for venue in self.venues:
            name = venue['name']
            if name in self.locations:
                continue
            self._fetch_new_locations(name)

    def _fetch_new_locations(self, name):
        for res in self._get_place_details(name):
            address = res['formatted_address']
            geometry_location = res['geometry']['location']
            latitude, longitude = (geometry_location['lat'], geometry_location['lng'])
            location = {'name': name, 'address': address, 'latitude': latitude, 'longitude': longitude}
            self.locations.setdefault(name, []).append(location)
            print('    {:<40s}{:<60s}{:>12.1f}{:>12.1f}'.format(name, address, latitude, longitude))

    def _write_locations(self):
        print('Writing updated locations...'.ljust(LINE_LENGTH), end=' ')
        new_locations_file = NamedTemporaryFile(delete=False)
        with open(new_locations_file.name, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self.LOCATION_FIELDNAMES, delimiter='|')
            writer.writeheader()
            for key, locations in self.locations.items():
                for location in locations:
                    writer.writerow(location)

        pretty_file(new_locations_file.name,
                    header=False,
                    border=False,
                    delimiter='|',
                    new_filename=self.locations_file)

        print('Done')

    def _write_venues(self):
        print('Writing updated venues...'.ljust(LINE_LENGTH), end=' ')
        new_venues_file = NamedTemporaryFile(delete=False)
        with open(new_venues_file.name, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self.VENUES_FIELDNAMES, delimiter='|')
            writer.writeheader()
            for venue in self.venues:
                writer.writerow(venue)

        pretty_file(new_venues_file.name,
                    header=False,
                    border=False,
                    delimiter='|',
                    new_filename=self.venues_file)
        print('Done')

    @staticmethod
    def _fetch_location(adress):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        gmaps = googlemaps.Client(key=gmaps_api_key)
        geocode_result = gmaps.geocode(adress)
        for res in geocode_result:
            coords = res['geometry']['location']
            return [coords['lat'], coords['lng']]

    def _get_place_details(self, name):
        if name not in self.places:
            self._fetch_place_details(name)
        # If no results were found on Google save empty result
        if name not in self.places:
            self.places[name] = []
        return self.places[name]

    def _fetch_place_details(self, name):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        client = googlemaps.Client(key=gmaps_api_key)
        result = client.find_place(name, 'textquery',
                                   fields=['place_id'],
                                   location_bias='ipbias')
        for res in result['candidates']:
            place_id = res['place_id']
            place_data = client.place(place_id, fields=['website',
                                                        'international_phone_number',
                                                        'opening_hours',
                                                        'formatted_address',
                                                        'geometry'])
            self.places.setdefault(name, []).append(place_data['result'])

    def __repr__(self):
        return '[UpdateLocationsCommand ({})]'.format(self.locations_file)
