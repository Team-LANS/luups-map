"""DTOs related to vouchers."""


class VoucherDto(object):
    __slots__ = 'id', 'id_venue', 'description', 'voucher_types', 'voucher_tags'

    def __init__(self, data):
        self.id = data.id
        self.id_venue = data.id_venue
        self.description = data.description
        self.voucher_types = [entry.type for entry in data.voucher_types] if data.voucher_types else []
        self.voucher_tags = [entry.tag for entry in data.voucher_tags] if data.voucher_tags else []


class VoucherTypeDto(object):
    __slots__ = 'id', 'id_voucher', 'type'

    def __init__(self, data):
        self.id_voucher = data.id_voucher
        self.type = data.type


class VoucherTagDto(object):
    __slots__ = 'id', 'id_voucher', 'tag'

    def __init__(self, data):
        self.id_voucher = data.id_voucher
        self.tag = data.tag
