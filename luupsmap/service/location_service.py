from luupsmap import db
from luupsmap.model import Location
from luupsmap.dto import LocationDto
from luupsmap.service import as_dto
from luupsmap.service.search import LocationSearch


class LocationService:
    def __init__(self):
        self.db_session = db.session

    def find_all(self, params):
        return self.__find_all()

    @as_dto(LocationDto)
    def __find_all(self, params):
        return LocationSearch().apply(params)

    @as_dto(LocationDto)
    def get(self, location_id):
        return self.db_session.query(Location).get(location_id)
