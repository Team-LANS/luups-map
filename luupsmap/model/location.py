"""A model for venue locations."""
from sqlalchemy.orm import relationship

from luupsmap import db


class Location(db.Model):
    __tablename__ = 'location'

    id = db.Column(db.Integer, primary_key=True)
    id_venue = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    address = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(64))
    phone = db.Column(db.String(32))
    opening_hours = db.relationship("Interval", backref="location")
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)

    def __init__(self, data):
        self.address = data['address']
        self.email = data['email']
        self.phone = data['phone']
        self.opening_hours = data['opening_hours']
        self.latitude = data['latitude']
        self.longitude = data['longitude']
        self.venue = data['venue']

    def __repr__(self):
        return '<LOCATION "{}">'.format(self.address)
