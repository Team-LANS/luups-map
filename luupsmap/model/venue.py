"""Model for restaurants, bars and event locations that accept vouchers."""

from luupsmap import db
from luupsmap.model.enum.venue_type import VenueType


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text())
    venue_type = db.Column(db.Enum(VenueType), nullable=False)
    homepage = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(32))
    opening_hours = db.Column(db.Text())
    os = db.Column(db.Text())
    address = db.Column(db.String(256), nullable=False)
    latitude = db.Column(db.Float(), nullable=False)
    longitude = db.Column(db.Float(), nullable=False)

    def __init__(self, name, description, venue_type, homepage, email, phone, opening_hours, address):
        self.name = name
        self.description = description
        self.venue_type = venue_type
        self.homepage = homepage
        self.email = email
        self.phone = phone
        self.opening_hours = opening_hours
        self.address = address
        self.latitude = 0.0
        self.longitude = 0.0

    def __repr__(self):
        return '[Venue "{}" ({})]'.format(self.name, repr(self.venue_type))
