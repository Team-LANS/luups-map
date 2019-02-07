import os

from flask.cli import AppGroup, with_appcontext
from sqlalchemy import text

from luupsmap import app, db
from luupsmap.model import Venue

LINE_LENGTH = 25

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
    print('Removing existing data...'.ljust(LINE_LENGTH), end=' ')
    session = db.session
    session.query(Venue) \
        .delete()
    session.commit()
    print('Done')


def seed_data():
    print('Start seeding tables...'.ljust(LINE_LENGTH), end=' ')
    path = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(path, '..', '..', 'data', 'venues.sql')
    file = open(file_path)
    sql = text(file.read())
    db.engine.execute(sql)
    print('Done')


app.cli.add_command(db_utils)
