from flask.cli import AppGroup, with_appcontext
from sqlalchemy.orm import Session

from luupsmap import app, db

from luupsmap.model.venue import Venue
from luupsmap.model.enum.venue_type import VenueType

db_utils = AppGroup('data')


@db_utils.command('seed')
@with_appcontext
def seed():
    print('Start seeding')
    session = db.session

    objects = [
        Venue('name', 'description', VenueType.BAR, ';test', 'email', 'phone', 'opening_hours', 'address',),
    ]
    session.bulk_save_objects(objects)
    session.commit()


app.cli.add_command(db_utils)
