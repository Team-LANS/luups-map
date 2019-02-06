import os

from flask.cli import AppGroup, with_appcontext
from sqlalchemy import text

from luupsmap import app, db

from luupsmap.model.venue import Venue
from luupsmap.model.enum.venue_type import VenueType

db_utils = AppGroup('data')


@db_utils.command('seed')
@with_appcontext
def seed():
    remove_data()
    seed_data()


@db_utils.command('reset')
@with_appcontext
def reset():
    remove_data()


def remove_data():
    print('Removing existing data...', end=' ')
    session = db.session
    session.query(Venue).delete()
    session.commit()
    print('Done')


def seed_data():
    print('Start seeding tables...', end=' ')
    file_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(file_path, "../../data/venues.sql")
    file = open(path)
    sql = text(file.read())
    result = db.engine.execute(sql)
    print('Done')

app.cli.add_command(db_utils)

