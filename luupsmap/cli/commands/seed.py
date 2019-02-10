import csv
from tempfile import NamedTemporaryFile

from luupsmap import db
from luupsmap.cli.csv_helper import strip_whitepace
from luupsmap.model import Venue, Location

LINE_LENGTH = 25


class SeedCommand:

    def __init__(self, venues_file, locations_file, vouchers_file):
        self.venues_file = venues_file
        self.locations_file = locations_file
        self.vouchers_file = vouchers_file

    def run(self):
        print('Start seeding tables...'.ljust(LINE_LENGTH), end=' ')
        processed_venues_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.venues_file, processed_venues_file)
        venues = self._load_venues()
        locations = self._load_locations(venues)
        db.session.add_all(venues.values())
        db.session.add_all(locations)
        db.session.commit()

        print('Done')

    def _load_venues(self):
        processed_venues_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.venues_file, processed_venues_file)
        venues = {}
        with open(processed_venues_file.name, 'r') as venues_file:
            reader = csv.DictReader(venues_file, delimiter='|')
            for row in reader:
                row['locations'] = []
                row['vouchers'] = []
                venue = Venue(row)
                venues[row['name']] = venue
        return venues

    def _load_locations(self, venues):
        processed_locations_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.locations_file, processed_locations_file)
        locations = []
        with open(processed_locations_file.name, 'r') as venues_file:
            reader = csv.DictReader(venues_file, delimiter='|')
            for row in reader:
                venue = venues[row['name']]
                row['venue'] = venue
                location = Location(row)
                locations.append(location)
        return locations


    def __repr__(self):
        return '[SeedCommand ({}, {}, {})]'.format(self.venues_file, self.locations_file, self.vouchers_file)
