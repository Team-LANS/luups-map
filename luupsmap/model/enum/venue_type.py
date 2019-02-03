from enum import Enum


class VenueType(Enum):
    RESTAURANT = 'RESTAURANT'
    BAR = 'BAR'
    VENUE = 'VENUE'

    def __repr__(self):
        return self.value.lower()
