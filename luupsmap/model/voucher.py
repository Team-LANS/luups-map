"""The voucher model."""
from luupsmap import db
from luupsmap.model import Tag, Type


class Voucher(db.Model):
    __tablename__ = 'voucher'

    id = db.Column(db.Integer, primary_key=True)
    id_venue = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    description = db.Column(db.Text, nullable=False)

    voucher_types = db.relationship("VoucherType")
    voucher_tags = db.relationship("VoucherTag")

    def __init__(self, data):
        self.venue = data['venue']
        self.description = data['description']
        self.voucher_types = data['voucher_types']
        self.voucher_tags = data['voucher_tags']

    def __repr__(self):
        return '<VOUCHER "{}">'.format(self.id)


class VoucherType(db.Model):
    __tablename__ = 'voucher_type'

    id_voucher = db.Column(db.Integer, db.ForeignKey('voucher.id'), primary_key=True, nullable=False)
    type = db.Column(db.Enum(Type), primary_key=True, nullable=False)

    def __init__(self, voucher_type):
        self.type = voucher_type

    def __repr__(self):
        return '<VOUCHERTYPE "{}: {}">'.format(self.id_voucher, self.type)


class VoucherTag(db.Model):
    __tablename__ = 'voucher_tag'

    id_voucher = db.Column(db.Integer, db.ForeignKey('voucher.id'), primary_key=True, nullable=False)
    tag = db.Column(db.Enum(Tag), nullable=False, primary_key=True)

    def __init__(self, tag):
        self.tag = tag

    def __repr__(self):
        return '<VOUCHERTAG "{}: {}">'.format(self.id_voucher, self.tag)
