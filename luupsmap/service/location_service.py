from luupsmap import db
from luupsmap.model import Location
from luupsmap.dto import LocationDto
from luupsmap.service import as_dto


class LocationService:
    def __init__(self):
        self.db_session = db.session

    def find_all(self):
        return self.__find_all()

    @as_dto(LocationDto)
    def __find_all(self):
        return self.db_session.query(Location).all()

    @as_dto(LocationDto)
    def get(self, location_id):
        return self.db_session.query(Location).get(location_id)
