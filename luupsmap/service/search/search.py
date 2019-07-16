from luupsmap import db
from luupsmap.model import Location, Interval, Venue, VoucherTag, VoucherType


class LocationSearch:

    def __init__(self):
        self.db_session = db.session
        self.base = db.session.query(Location).join(Venue)

    def apply(self, params):
        if params['opening_hours']:
            self.__search_by_time(params['voucher_tags'])
        if params['voucher_types']:
            self.__search_by_voucher_tags(params['voucher_types'])
        if params['voucher_tags']:
            self.__search_by_voucher_types(params['voucher_tags'])
        return self.base.all()

    def __search_by_voucher_tags(self, tags):
        self.base = self.base \
            .join(VoucherTag) \
            .filter(VoucherTag.tag.in_(tags))

    def __search_by_voucher_types(self, types):
        self.base = self.base \
            .join(VoucherType) \
            .filter(VoucherType.type.in_(types))

    def __search_by_time(self, time):
        weekday = time.weekday()
        month = time.month
        time = time.time()
        self.base = self.base \
            .outerjoin(Interval) \
            .filter(time >= Interval.start_hour,
                    time <= Interval.end_hour,
                    weekday >= Interval.start_day,
                    weekday <= Interval.end_day,
                    month >= Interval.start_month,
                    month <= Interval.end_month)
