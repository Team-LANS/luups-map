"""A Model for restaurants, bars and event locations that accept vouchers."""

from luupsmap import db


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    homepage = db.Column(db.String(64))
    email = db.Column(db.String(64))
    phone = db.Column(db.String(32))
    opening_hours = db.Column(db.Text)

    # relationships
    vouchers = db.relationship('Voucher')
    locations = db.relationship('Location')

    def __init__(self, data):
        self.id = data.id
        self.name = data.name
        self.description = data.description
        self.homepage = data.homepage
        self.email = data.email
        self.phone = data.phone
        self.opening_hours = data.opening_hours

        self.vouchers = data.vouchers
        self.locations = data.locations

    def __repr__(self):
        return '<VENUE "{}">'.format(self.name)
