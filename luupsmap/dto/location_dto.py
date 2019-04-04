"""Location DTOs."""


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
        self.opening_hours = data.opening_hours
