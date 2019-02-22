import csv
from tempfile import NamedTemporaryFile

import googlemaps

from luupsmap.cli.csv_helper import strip_whitepace, pretty_file
from luupsmap import app

LINE_LENGTH = 25


class UpdateAddressesCommand:
    locations = {}
    venues = []

    def __init__(self, locations_file, venues_file):
        self.locations_file = locations_file
        self.venues_file = venues_file

    def run(self):
        self._load_venues()
        self._load_locations()
        self._update_locations()
        self._write_locations()

    def _load_venues(self):
        print('Loading venues file...'.ljust(LINE_LENGTH), end=' ')
        processed_venues_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.venues_file, processed_venues_file)
        with open(processed_venues_file.name, 'r') as infile:
            reader = csv.DictReader(infile, delimiter='|')
            for row in reader:
                key = row['name']
                self.venues.append(key)
        print('Done')

    def _load_locations(self):
        print('Loading address file...'.ljust(LINE_LENGTH), end=' ')
        processed_address_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.locations_file, processed_address_file)
        with open(processed_address_file.name, 'r') as infile:
            reader = csv.DictReader(infile, delimiter='|')
            for row in reader:
                key = row['name']
                if key in self.locations:
                    self.locations[key].append(row)
                else:
                    self.locations[key] = [row]

        print('Done')

    def _update_locations(self):
        print('Fetching new locations...'.ljust(LINE_LENGTH))
        for name in self.venues:
            if name in self.locations:
                continue
            self._fetch_locations(name)

    def _fetch_locations(self, name):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        client = googlemaps.Client(key=gmaps_api_key)
        result = client.find_place(name, 'textquery',
                                   fields=['place_id', 'formatted_address', 'geometry'],
                                   location_bias='ipbias')
        for res in result['candidates']:
            address = res['formatted_address']
            geometry_location = res['geometry']['location']
            latitude, longitude = (geometry_location['lat'], geometry_location['lng'])
            location = {'name': name, 'address': address, 'latitude': latitude, 'longitude': longitude}
            self.locations.setdefault(name, []).append(location)
            print('    {:<40s}{:<60s}{:>12.1f}{:>12.1f}'.format(name, address, latitude, longitude))

    def _write_locations(self):
        print('Writing new locations...'.ljust(LINE_LENGTH), end=' ')
        new_locations_file = NamedTemporaryFile(delete=False)
        with open(new_locations_file.name, 'w') as outfile:
            fieldnames = ['name', 'address', 'latitude', 'longitude']
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter='|')
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


def __repr__(self):
    return '[UpdateLocationsCommand ({})]'.format(self.locations_file)
