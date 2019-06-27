"""A Model for restaurants, bars and event locations that accept vouchers."""

from luupsmap import db


class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    homepage = db.Column(db.String(64))

    locations = db.relationship("Location", backref="venue")
    vouchers = db.relationship("Voucher", backref="venue")

    def __init__(self, data=None):
        if data is None:
            return

        self.name = data['name']
        self.description = data['description']
        self.homepage = data['homepage']

        self.vouchers = data['vouchers']
        self.locations = data['locations']

    def add_voucher(self, voucher):
        self.vouchers.append(voucher)

    def add_location(self, location):
        self.locations.append(location)

    def __repr__(self):
        return '<VENUE "{}">'.format(self.name)
