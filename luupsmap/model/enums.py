from enum import Enum


class Type(Enum):
    FOOD = 1
    DRINK = 2
    TICKET = 4

    def __repr__(self):
        return self.name.lower()

    @classmethod
    def value_sum(cls):
        """Calculate the sum of all values."""
        return 2 ** len(cls.__members__.keys()) - 1


class Tag(Enum):
    BREAKFAST = 'BREAKFAST'
    MAIN_COURSE = 'MAIN_COURSE'
    SNACK = 'SNACK'
    PASTRIES = 'PASTRIES'
    ICE_CREAM = 'ICE_CREAM'

    COFFEE = 'COFFEE'
    ALCOHOL = 'ALCOHOL'

    EVENT = 'EVENT'
    TICKET = 'TICKET'
    GUIDED_TOUR = 'GUIDED_TOUR'
    WORKSHOP = 'WORKSHOP'

    SHOPPING = 'SHOPPING'
    FREE_GIFT = 'FREE_GIFT'

    COMBINATION = 'COMBINATION'
    SEASONAL = 'SEASONAL'

    def __repr__(self):
        return self.value.lower()
