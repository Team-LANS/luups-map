from luupsmap import db
from luupsmap.model import Location
from luupsmap.dto import LocationDto
from luupsmap.service import as_dto


class LocationService:
    def __init__(self):
        self.db_session = db.session

    @as_dto(LocationDto)
    def get(self, location_id):
        return self.db_session.query(Location).get(location_id)
