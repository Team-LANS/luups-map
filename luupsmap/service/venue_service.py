from dto.venue_dto import VenueDto, VenueDetailDto
from luupsmap import db
from luupsmap.model import Venue
from service import as_dto


class VenueService:
    def __init__(self):
        self.db_session = db.session
        self.entity = Venue

    @as_dto(VenueDto)
    def find_all(self):
        return self.db_session.query(self.entity).all()

    @as_dto(VenueDetailDto)
    def get(self, venue_id):
        return self.db_session.query(self.entity).get(venue_id)
