import csv
import os
import re
from tempfile import NamedTemporaryFile

import googlemaps
from sqlalchemy import text

from cli.csv_helper import strip_whitepace, pretty_file
from luupsmap import app, db

LINE_LENGTH = 25


class UpdateLocationsCommand:
    def __init__(self, address_file):
        self.address_file = address_file

    def run(self):
        print('Preprocessing data file...'.ljust(LINE_LENGTH), end=' ')
        processed_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.address_file, processed_file)
        print('Done')
        updated_file = NamedTemporaryFile(delete=False)
        print('Adding missing coordinates...'.ljust(LINE_LENGTH))
        self._fetch_locations(processed_file, updated_file)

        print('Updating existing file...'.ljust(LINE_LENGTH), end=' ')
        # TODO: Sort the data too
        pretty_file(updated_file.name,
                    header=False,
                    border=False,
                    delimiter='|',
                    new_filename=self.address_file)
        print('Done')

    def __repr__(self):
        return '[UpdateLocationsCommand ({})]'.format(self.address_file)

    def _fetch_locations(self, infile, outfile):
        with open(infile.name, 'r') as infile:
            reader = csv.DictReader(infile, delimiter='|')
            with open(outfile.name, 'w') as outfile:
                writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter='|')
                writer.writeheader()
                for row in reader:
                    self._add_missing_coordinates(row)
                    writer.writerow(row)

    def _add_missing_coordinates(self, row):
        coordinates_missing = row['latitude'] in (None, '') or row['longitude'] in (None, '')
        address = row['address']
        if coordinates_missing and address not in (None, ''):
            [latitude, longitude] = self._fetch_location(address)
            row['latitude'] = latitude
            row['longitude'] = longitude
            change = '%s : %s, %s' % (row['name'], latitude, longitude)
            print(' ' * 4 + change)

    @staticmethod
    def _fetch_location(adress):
        gmaps_api_key = app.config['GMAPS_API_KEY']
        gmaps = googlemaps.Client(key=gmaps_api_key)
        geocode_result = gmaps.geocode(adress)
        for res in geocode_result:
            coords = res['geometry']['location']
            return [coords['lat'], coords['lng']]
