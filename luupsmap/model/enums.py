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

    TICKET = 'TICKET'
    GUIDED_TOUR = 'GUIDED_TOUR'
    WORKSHOP = 'WORKSHOP'

    SHOPPING = 'SHOPPING'
    FREE_GIFT = 'FREE_GIFT'

    COMBINATION = 'COMBINATION'

    @classmethod
    def translation(cls, tag):
        translations = {
            Tag.BREAKFAST: 'Frühstück',
            Tag.MAIN_COURSE: 'Hauptmahlzeit',
            Tag.SNACK: 'Snack',
            Tag.PASTRIES: 'Gebäck',
            Tag.ICE_CREAM: 'Eis',
            Tag.COFFEE: 'Kaffee',
            Tag.ALCOHOL: 'Alkoholhaltiges',
            Tag.TICKET: 'Ticket',
            Tag.GUIDED_TOUR: 'Führung',
            Tag.WORKSHOP: 'Workshop',
            Tag.SHOPPING: 'Shopping',
            Tag.FREE_GIFT: 'Gratis',
            Tag.COMBINATION: 'Kombination'
        }
        return translations[tag]

    def __repr__(self):
        return self.name.lower()
