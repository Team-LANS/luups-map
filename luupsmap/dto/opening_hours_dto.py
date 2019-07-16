"""DTOs related to intervals."""
from luupsmap.service.opening_hour_service import OpeningHourService


class OpeningHoursDto(object):
    __slots__ = 'id', 'id_location', 'entries'

    def __init__(self, location):
        self.id_location = location.id
        self.entries = OpeningHourService(location).get_readable()
