"""Venue Dtos."""


class VenueDto(object):
    """Short venue dto containing only the most important attributes."""
    __slots__ = 'id', 'name', 'venue_type', 'homepage', 'address', 'latitude', 'longitude', '__dict__'

    def __init__(self, venue):
        self.id = venue.id
        self.name = venue.name
        self.venue_type = venue.venue_type.value
        self.homepage = venue.homepage
        self.address = venue.address
        self.latitude = venue.latitude
        self.longitude = venue.longitude


class VenueDetailDto(VenueDto):
    """Venue dto containing all details known about the venue."""
    __slots__ = 'description', 'email', 'phone', 'opening_hours'

    def __init__(self, venue):
        super().__init__(venue)
        self.description = venue.description
        self.email = venue.email
        self.phone = venue.phone
        self.opening_hours = venue.opening_hours
