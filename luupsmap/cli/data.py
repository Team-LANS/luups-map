import os

from flask.cli import AppGroup, with_appcontext

from luupsmap.cli.commands import SeedCommand, UpdateLocationsCommand
from luupsmap import app, db
from luupsmap.model import Venue, Location, Voucher

LINE_LENGTH = 25

data = AppGroup('data')


@data.command('seed')
@with_appcontext
def seed():
    remove_data()
    path = os.path.abspath(os.path.dirname(__file__))
    venues_file = os.path.join(path, '..', '..', 'data', 'venues.csv')
    locations_file = os.path.join(path, '..', '..', 'data', 'locations.csv')
    vouchers_file = os.path.join(path, '..', '..', 'data', 'vouchers.csv')
    SeedCommand(venues_file, locations_file, vouchers_file).run()


@data.command('reset')
@with_appcontext
def reset():
    remove_data()


@data.command('update-locations')
@with_appcontext
def update():
    path = os.path.abspath(os.path.dirname(__file__))
    infile = os.path.join(path, '..', '..', 'data', 'locations.csv')
    UpdateLocationsCommand(infile).run()


def remove_data():
    # TODO: Use logger
    print('Removing existing data...'.ljust(LINE_LENGTH), end=' ')
    session = db.session
    session.query(Location).delete()
    session.query(Voucher).delete()
    session.query(Venue).delete()
    session.commit()
    print('Done')


app.cli.add_command(data)
