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
        self.venue = data['venue']
        self.start_hour = data['start_hour']
        self.end_hour = data['end_hour']
        self.start_day = data['start_day']
        self.end_day = data['end_day']
        self.start_month = data['start_month']
        self.end_month = data['end_month']

    def __repr__(self):
        return '<INTERVAL "{}">'.format(self.id)


