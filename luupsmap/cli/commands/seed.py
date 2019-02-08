from sqlalchemy import text

from luupsmap import db

LINE_LENGTH = 25


class SeedCommand:

    def __init__(self, data_file):
        self.data_file = data_file

    def run(self):
        print('Start seeding tables...'.ljust(LINE_LENGTH), end=' ')
        file = open(self.data_file)
        sql = text(file.read())
        # TODO: Use CSV directly
        db.engine.execute(sql)
        print('Done')

    def __repr__(self):
        return '[SeedCommand ({})]'.format(self.data_file)
