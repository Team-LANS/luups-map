"""Location DTOs."""

from luupsmap.dto import OpeningHoursDto


class LocationDto(object):
    __slots__ = 'id', 'id_venue', 'address', 'latitude', 'longitude', 'email', 'phone', 'opening_hours'

    def __init__(self, data):
        self.id = data.id
        self.id_venue = data.id_venue
        self.address = data.address
        self.latitude = data.latitude
        self.longitude = data.longitude
        self.email = data.email
        self.phone = data.phone
        self.opening_hours = OpeningHoursDto(data)


class LocationSearchDto(object):
    __slots__ = 'opening_time', 'voucher_tags', 'voucher_types'

    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])
