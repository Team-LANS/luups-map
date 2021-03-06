from luupsmap import db
from luupsmap.cli.util import CsvFile
from luupsmap.model import Venue, Location, Voucher, VoucherType, VoucherTag, Type, Tag


class SeedCommand:
    venues = []
    locations = {}
    vouchers = {}

    def __init__(self, venues_file, locations_file, vouchers_file):
        self.venues_file = CsvFile(venues_file, ['name', 'homepage', 'description'])
        self.locations_file = CsvFile(locations_file,
                                      ['name', 'address', 'email', 'phone', 'opening_hours', 'latitude', 'longitude'])
        self.vouchers_file = CsvFile(vouchers_file,
                                     ['name', 'description', 'limitations', 'voucher_tags', 'voucher_types'])

    def run(self):
        print('Start seeding tables...'.ljust(25), end=' ')
        self.venues = self.venues_file.load()
        self._load_locations()
        self._load_vouchers()
        self._create_and_save_models()
        print('Done')

    def _load_locations(self):
        locations = self.locations_file.load()
        for location in locations:
            name = location['name']
            self.locations.setdefault(name, []).append(location)

    def _load_vouchers(self):
        vouchers = self.vouchers_file.load()
        for voucher in vouchers:
            name = voucher['name']
            self.vouchers.setdefault(name, []).append(voucher)

    def _create_and_save_models(self):
        venues = []
        locations = []
        vouchers = []
        for venue in self.venues:
            venue['vouchers'] = []
            venue['locations'] = []
            venue = Venue(venue)
            self._create_locations(venue, locations)
            self._create_vouchers(venue, vouchers)
        db.session.add_all(venues)
        db.session.add_all(locations)
        db.session.add_all(vouchers)
        db.session.commit()

    def _create_locations(self, venue, locations):
        name = venue.name
        if name not in self.locations:
            return
        for location in self.locations[name]:
            location['venue'] = venue
            location = Location(location)
            venue.locations.append(location)
            locations.append(location)

    def _create_vouchers(self, venue, vouchers):
        name = venue.name
        if name not in self.vouchers:
            return
        for voucher in self.vouchers[name]:
            self._convert_voucher_types(voucher)
            self._convert_voucher_tags(voucher)
            voucher['venue'] = venue
            voucher = Voucher(voucher)
            venue.vouchers.append(voucher)
            vouchers.append(voucher)

    @staticmethod
    def _convert_voucher_types(voucher):
        # In case we already converted string to proper types
        if type(voucher['voucher_types']) == list:
            return
        voucher_types = [x.strip() for x in voucher['voucher_types'].split(',')]
        voucher['voucher_types'] = [VoucherType(Type[voucher_type]) for voucher_type in voucher_types]

    @staticmethod
    def _convert_voucher_tags(voucher):
        # In case we already converted string to proper types
        if type(voucher['voucher_tags']) == list:
            return
        if voucher['voucher_tags'] == '':
            voucher['voucher_tags'] = []
            return
        voucher_tags = [x.strip() for x in voucher['voucher_tags'].split(',')]
        voucher['voucher_tags'] = [VoucherTag(Tag[voucher_tag]) for voucher_tag in voucher_tags]


def __repr__(self):
    return '[SeedCommand ({}, {}, {})]'.format(self.venues_file, self.locations_file, self.vouchers_file)
