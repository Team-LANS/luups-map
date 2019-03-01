from luupsmap.cli.util import CsvFile, PlaceCache

LINE_LENGTH = 25


class UpdateCommand:
    locations = {}
    places = {}
    venues = []

    def __init__(self, locations_file, venues_file):
        self.locations_file = CsvFile(locations_file, ['name', 'address', 'latitude', 'longitude'])
        self.venues_file = CsvFile(venues_file, ['name', 'homepage', 'email', 'phone', 'opening_hours', 'description'])
        self.place_cache = PlaceCache()

    def run(self):
        self._load_venues()
        self._load_locations()
        self._update_venues()
        self._update_locations()
        self._create_locations()
        self._write_files()

    def _load_venues(self):
        print('Loading venues file...'.ljust(LINE_LENGTH), end=' ')
        self.venues = self.venues_file.load()
        print('Done')

    def _load_locations(self):
        print('Loading address file...'.ljust(LINE_LENGTH), end=' ')
        locations = self.locations_file.load()
        for location in locations:
            name = location['name']
            self.locations.setdefault(name, []).append(location)
        print('Done')

    def _update_venues(self):
        print('Updating venues...'.ljust(LINE_LENGTH))
        for venue in self.venues:
            empty_fields = self._empty_fields(venue)
            if not empty_fields:
                continue
            if 'homepage' in empty_fields or 'phone' in empty_fields and 'email' not in empty_fields:
                self._update_venue(venue)
        print('Done')

    def _update_venue(self, venue):
        name = venue['name']
        place_details = self.place_cache.get(name)
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
                detail = self.place_cache.get(name)[0]
                geometry_location = detail['geometry']['location']
                latitude, longitude = (geometry_location['lat'], geometry_location['lng'])
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
        for res in self.place_cache.get(name):
            address = res['formatted_address']
            geometry_location = res['geometry']['location']
            latitude, longitude = (geometry_location['lat'], geometry_location['lng'])
            location = {'name': name, 'address': address, 'latitude': latitude, 'longitude': longitude}
            self.locations.setdefault(name, []).append(location)
            print('    {:<40s}{:<60s}{:>12.1f}{:>12.1f}'.format(name, address, latitude, longitude))

    def _write_files(self):
        print('Writing updated files...'.ljust(LINE_LENGTH))
        self.venues_file.write(self.venues)
        locations = [sublist for parentlist in self.locations.values() for sublist in parentlist]
        self.locations_file.write(locations)
        print('Done')
