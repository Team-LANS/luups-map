import csv
import os
import re
from tempfile import NamedTemporaryFile

import googlemaps

from luupsmap import app

LINE_LENGTH = 25


def update_data(file):
    print('Preprocessing data file...'.ljust(LINE_LENGTH), end=' ')
    processed_file = NamedTemporaryFile(delete=False)
    strip_whitepace(file, processed_file)
    print('Done')
    updated_file = NamedTemporaryFile(delete=False)
    print('Adding missing coordinates...'.ljust(LINE_LENGTH))
    fetch_locations(processed_file, updated_file)

    print('Updating existing file...'.ljust(LINE_LENGTH), end=' ')
    # TODO: Sort the data too
    pretty_file(updated_file.name,
                header=False,
                border=False,
                delimiter='|',
                new_filename=file)
    print('Done')


def strip_whitepace(infile, outfile):
    with open(infile, 'r') as infile, open(outfile.name, 'w') as outfile:
        for line in infile:
            line = re.sub(r'\|\s*', '|', line)
            line = re.sub(r'\s*\|', '|', line)
            outfile.write(line)


def fetch_locations(infile, outfile):
    with open(infile.name, 'r') as infile:
        reader = csv.DictReader(infile, delimiter='|')
        with open(outfile.name, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames, delimiter='|')
            writer.writeheader()
            for row in reader:
                add_missing_coordinates(row)
                writer.writerow(row)


def add_missing_coordinates(row):
    coordinates_missing = row['latitude'] in (None, '') or row['longitude'] in (None, '')
    address = row['address']
    if coordinates_missing and address not in (None, ''):
        [latitude, longitude] = fetch_location(address)
        row['latitude'] = latitude
        row['longitude'] = longitude
        change = '%s : %s, %s' % (row['name'], latitude, longitude)
        print(' ' * 4 + change)


def fetch_location(adress):
    gmaps_api_key = app.config['GMAPS_API_KEY']
    gmaps = googlemaps.Client(key=gmaps_api_key)
    geocode_result = gmaps.geocode(adress)
    for res in geocode_result:
        coords = res['geometry']['location']
        return [coords['lat'], coords['lng']]


# Straight up stolen from:
# https://stackoverflow.com/questions/20025235/how-to-pretty-print-a-csv-file-in-python
# noinspection PyIncorrectDocstring
def pretty_file(filename, **options):
    """
    @summary:
        Reads a CSV file and prints visually the data as table to a new file.
    @param filename:
        is the path to the given CSV file.
    @param **options:
        the union of Python's Standard Library csv module Dialects and Formatting Parameters and the following list:
    @param new_delimiter:
        the new column separator (default ' | ')
    @param border:
        boolean value if you want to print the border of the table (default True)
    @param border_vertical_left:
        the left border of the table (default '| ')
    @param border_vertical_right:
        the right border of the table (default ' |')
    @param border_horizontal:
        the top and bottom border of the table (default '-')
    @param border_corner_tl:
        the top-left corner of the table (default '+ ')
    @param border_corner_tr:
        the top-right corner of the table (default ' +')
    @param border_corner_bl:
        the bottom-left corner of the table (default same as border_corner_tl)
    @param border_corner_br:
        the bottom-right corner of the table (default same as border_corner_tr)
    @param header:
        boolean value if the first row is a table header (default True)
    @param border_header_separator:
        the border between the header and the table (default same as border_horizontal)
    @param border_header_left:
        the left border of the table header (default same as border_corner_tl)
    @param border_header_right:
        the right border of the table header (default same as border_corner_tr)
    @param newline:
        defines how the rows of the table will be separated (default '\n')
    @param new_filename:
        the new file's filename (*default* '/new_' + filename)
    """

    # function specific options
    new_delimiter = options.pop('new_delimiter', ' | ')
    border = options.pop('border', True)
    border_vertical_left = options.pop('border_vertical_left', '| ')
    border_vertical_right = options.pop('border_vertical_right', ' |')
    border_horizontal = options.pop('border_horizontal', '-')
    border_corner_tl = options.pop('border_corner_tl', '+ ')
    border_corner_tr = options.pop('border_corner_tr', ' +')
    border_corner_bl = options.pop('border_corner_bl', border_corner_tl)
    border_corner_br = options.pop('border_corner_br', border_corner_tr)
    header = options.pop('header', True)
    border_header_separator = options.pop('border_header_separator', border_horizontal)
    border_header_left = options.pop('border_header_left', border_corner_tl)
    border_header_right = options.pop('border_header_right', border_corner_tr)
    newline = options.pop('newline', '\n')

    file_path = filename.split(os.sep)
    old_filename = file_path[-1]
    new_filename = options.pop('new_filename', 'new_' + old_filename)

    column_max_width = {}  # key:column number, the max width of each column
    num_rows = 0  # the number of rows

    with open(filename, 'r') as input:  # parse the file and determine the width of each column
        reader = csv.reader(input, **options)
        for row in reader:
            num_rows += 1
            for col_number, column in enumerate(row):
                width = len(column)
                try:
                    if width > column_max_width[col_number]:
                        column_max_width[col_number] = width
                except KeyError:
                    column_max_width[col_number] = width

    max_columns = max(
        # the max number of columns (having rows with different number of columns is no problem)
        column_max_width.keys()) + 1

    if max_columns > 1:
        total_length = sum(column_max_width.values()) + len(new_delimiter) * (max_columns - 1)
        left = border_vertical_left if border is True else ''
        right = border_vertical_right if border is True else ''
        left_header = border_header_left if border is True else ''
        right_header = border_header_right if border is True else ''

        with open(filename, 'r') as input:
            reader = csv.reader(input, **options)
            with open(new_filename, 'w') as output:
                for row_number, row in enumerate(reader):
                    max_index = len(row) - 1
                    for index in range(max_columns):
                        if index > max_index:
                            row.append(' ' * column_max_width[index])  # append empty columns
                        else:
                            diff = column_max_width[index] - len(row[index])
                            row[index] = row[index] + ' ' * diff  # append spaces to fit the max width

                    if row_number == 0 and border is True:  # draw top border
                        output.write(border_corner_tl + border_horizontal * total_length + border_corner_tr + newline)
                    output.write(left + new_delimiter.join(row) + right + newline)  # print the new row
                    if row_number == 0 and header is True:  # draw header's separator
                        output.write(left_header + border_header_separator * total_length + right_header + newline)
                    if row_number == num_rows - 1 and border is True:  # draw bottom border
                        output.write(border_corner_bl + border_horizontal * total_length + border_corner_br)
