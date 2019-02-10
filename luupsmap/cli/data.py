import os

from flask.cli import AppGroup, with_appcontext

from luupsmap import app, db
from luupsmap.model import Venue
from luupsmap.cli.commands.update_locations import update_locations
from luupsmap.cli.commands.seed import SeedCommand

LINE_LENGTH = 25

data = AppGroup('data')


@data.command('seed')
@with_appcontext
def seed():
    remove_data()
    path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(path, '..', '..', 'data', 'venues.sql')
    SeedCommand(file_path).run()


@data.command('reset')
@with_appcontext
def reset():
    remove_data()


@data.command('update')
@with_appcontext
def update():
    path = os.path.abspath(os.path.dirname(__file__))
    infile = os.path.join(path, '..', '..', 'data', 'venues.csv')
    update_locations(infile)


def remove_data():
    # TODO: Use logger
    print('Removing existing data...'.ljust(LINE_LENGTH), end=' ')
    session = db.session
    session.query(Venue) \
        .delete()
    session.commit()
    print('Done')


app.cli.add_command(data)
