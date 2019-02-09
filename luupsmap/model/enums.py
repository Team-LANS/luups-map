from enum import Enum


class Type(Enum):
    FOOD = 'FOOD'
    DRINK = 'DRINK'
    TICKET = 'TICKET'

    def __repr__(self):
        return self.value.lower()


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
