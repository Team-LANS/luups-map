from luupsmap import db
from model.venue import Venue


class VenueService:
    def __init__(self):
        self.db_session = db.session
        self.entity = Venue

    def find_all(self):
        return self.db_session.query(self.entity).all()
