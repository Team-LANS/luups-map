import os

from flask.cli import AppGroup, with_appcontext
from sqlalchemy import text

from cli.commands.update_data import update_data
from luupsmap import app, db
from luupsmap.model import Venue

LINE_LENGTH = 25

data = AppGroup('data')


@data.command('seed')
@with_appcontext
def seed():
    remove_data()
    seed_data()


@data.command('reset')
@with_appcontext
def reset():
    remove_data()


@data.command('update')
@with_appcontext
def update():
    path = os.path.abspath(os.path.dirname(__file__))
    infile = os.path.join(path, '..', '..', 'data', 'venues.csv')
    update_data(infile)


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


app.cli.add_command(data)
