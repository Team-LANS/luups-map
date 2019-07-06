"""The voucher model."""
from luupsmap import db
from luupsmap.model import Tag, Type


class Interval(db.Model):
    __tablename__ = 'interval'

    id = db.Column(db.Integer, primary_key=True)
    id_venue = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_hour = db.Column(db.Time, nullable=False)
    end_hour = db.Column(db.Time, nullable=False)
    start_day = db.Column(db.Integer, nullable=False)
    end_day = db.Column(db.Integer, nullable=False)
    start_month = db.Column(db.Integer, nullable=False)
    end_month = db.Column(db.Integer, nullable=False)

    def __init__(self, data):
        for key in data:
            setattr(self, key, data[key])

    def __repr__(self):
        return '<INTERVAL "{}">'.format(self.id)
