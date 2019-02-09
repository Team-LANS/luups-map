from luupsmap import db
from luupsmap.dto.venue_dto import VenueDto, VenueDetailDto
from luupsmap.model import Venue
from luupsmap.service import as_dto


class VenueService:
    def __init__(self):
        self.db_session = db.session

    @as_dto(VenueDto)
    def find_all(self):
        return self.db_session.query(Venue).all()

    @as_dto(VenueDetailDto)
    def get(self, venue_id):
        return self.db_session.query(Venue).get(venue_id)
