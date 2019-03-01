"""Venue DTOs."""
from flask import jsonify

from luupsmap.dto import VoucherDto, LocationDto


class VenueDto(object):
    """Short venue dto containing only the most important attributes."""
    __slots__ = 'id', 'name', 'homepage', 'vouchers', 'locations', 'type'

    def __init__(self, data):
        self.id = data.id
        self.name = data.name
        self.homepage = data.homepage

        self.vouchers = [VoucherDto(voucher) for voucher in data.vouchers] if data.vouchers else []
        self.locations = [LocationDto(location) for location in data.locations] if data.locations else []

        self.type = 0


class VenueDetailDto(VenueDto):
    """Venue dto containing all details known about the venue."""
    __slots__ = 'description', 'email', 'phone', 'opening_hours'

    def __init__(self, data):
        super().__init__(data)
        self.description = data.description
        self.email = data.email
        self.phone = data.phone
        self.opening_hours = data.opening_hours
