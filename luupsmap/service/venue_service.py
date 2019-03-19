from luupsmap import db
from luupsmap.dto.venue_dto import VenueDto, VenueDetailDto
from luupsmap.model import Venue, Voucher, VoucherType, VoucherTag
from luupsmap.service import as_dto


class VenueService:
    def __init__(self):
        self.db_session = db.session

    def find_all(self, include_type=True):
        venues = self.__find_all()

        if include_type:
            for venue in venues:
                venue.type = self.__determine_type(venue.vouchers)

        return venues

    def filter_by(self, types, tags):
        venues = self.__filter_by(types, tags)

        # TODO: Improve conversion to DTO so we dont' have to patch this afterwards
        for venue in venues:
            venue.type = self.__determine_type(venue.vouchers)

        return venues

    @as_dto(VenueDto)
    def __find_all(self):
        return self.db_session.query(Venue).all()

    @as_dto(VenueDto)
    def __filter_by(self, types, tags):
        venues = self.db_session.query(Venue) \
            .join(Voucher) \
            .join(VoucherType) \
            .outerjoin(VoucherTag)
        if types:
            venues = venues.filter(VoucherType.type.in_(types))
        if tags:
            venues = venues.filter(VoucherTag.tag.in_(tags))
        return venues.all()

    @as_dto(VenueDetailDto)
    def get(self, venue_id):
        return self.db_session.query(Venue).get(venue_id)

    @as_dto(VenueDto)
    def create(self, venue):
        self.db_session.add(venue)
        return self.db_session.commit()

    @staticmethod
    def __determine_type(vouchers):
        types = {voucher_type for voucher in vouchers for voucher_type in voucher.voucher_types}
        if types:
            return sum(voucher_type.value for voucher_type in types)

        return 0
