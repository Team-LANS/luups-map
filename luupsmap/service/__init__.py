from luupsmap.service.venue_service import *


# DECORATORS

def as_dto(dto_class):
    def decorate(func):
        def convert_to_dto(*args, **kwargs):
            result = func(*args, **kwargs)

            # handle list/tuple
            if isinstance(result, (list, tuple)):
                return [dto_class(element) for element in result]

            # handle single element
            return dto_class(result) if result else None

        return convert_to_dto

    return decorate
