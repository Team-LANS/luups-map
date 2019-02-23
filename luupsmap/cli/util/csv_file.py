import csv
from tempfile import NamedTemporaryFile

from cli.util.csv_helper import strip_whitepace, pretty_file


class CsvFile:

    def __init__(self, file, fieldnames):
        self.file = file
        self.fieldnames = fieldnames

    def load(self):
        processed_locations_file = NamedTemporaryFile(delete=False)
        strip_whitepace(self.file, processed_locations_file)
        locations = []
        with open(processed_locations_file.name, 'r') as venues_file:
            reader = csv.DictReader(venues_file, fieldnames=self.fieldnames, delimiter='|')
            next(reader, None)
            for row in reader:
                locations.append(row)
        return locations

    def write(self, locations):
        new_locations_file = NamedTemporaryFile(delete=False)
        with open(new_locations_file.name, 'w') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=self.fieldnames, delimiter='|')
            writer.writeheader()
            for location in locations:
                writer.writerow(location)

        pretty_file(new_locations_file.name,
                    header=False,
                    border=False,
                    delimiter='|',
                    new_filename=self.file)

