import os

from flask.cli import AppGroup, with_appcontext

from luupsmap.cli.commands import SeedCommand, UpdateCommand
from luupsmap import app, db
from luupsmap.model import Venue, Location, Voucher, VoucherType, VoucherTag, Interval

LINE_LENGTH = 25

data = AppGroup('data')


@data.command('seed')
@with_appcontext
def seed():
    """
    Resets the database, and seeds new data from CSV files

    Usage:

        flask data seed
    """
    remove_data()
    path = os.path.abspath(os.path.dirname(__file__))
    venues_file = os.path.join(path, '..', '..', 'data', 'venues.csv')
    locations_file = os.path.join(path, '..', '..', 'data', 'locations.csv')
    vouchers_file = os.path.join(path, '..', '..', 'data', 'vouchers.csv')
    SeedCommand(venues_file, locations_file, vouchers_file).run()


@data.command('reset')
@with_appcontext
def reset():
    """
    Removes all data from the database, but leaves columns as is.

    Usage:

        flask data reset
    """
    remove_data()


@data.command('nuke')
@with_appcontext
def reset():
    """
    Resets the database, dropping all tables.

    Usage:

        flask data nuke
    """
    nuke()


@data.command('update')
@with_appcontext
def update():
    """
    Updates the CSV documents available for data seeding by fetching data from the Google API.

    Usage:

        flask data nuke
    """
    path = os.path.abspath(os.path.dirname(__file__))
    locations = os.path.join(path, '..', '..', 'data', 'locations.csv')
    venues = os.path.join(path, '..', '..', 'data', 'venues.csv')
    UpdateCommand(locations_file=locations, venues_file=venues).run()


def remove_data():
    print('Removing existing data...'.ljust(LINE_LENGTH), end=' ')
    session = db.session
    session.query(VoucherTag).delete()
    session.query(VoucherType).delete()
    session.query(Voucher).delete()
    session.query(Interval).delete()
    session.query(Location).delete()
    session.query(Venue).delete()
    session.commit()
    print('Done')


def nuke():
    print('Dropping all tables and removing types...'.ljust(LINE_LENGTH), end=' ')
    session = db.session
    VoucherTag.__table__.drop(db.engine)
    VoucherType.__table__.drop(db.engine)
    Interval.__table__.drop(db.engine)
    Location.__table__.drop(db.engine)
    Voucher.__table__.drop(db.engine)
    Venue.__table__.drop(db.engine)
    session.execute('DROP TABLE alembic_version')
    session.commit()
    print('Done')


app.cli.add_command(data)
