"""DTOs related to vouchers."""


class VoucherDto(object):
    __slots__ = 'description', 'limitations', 'voucher_types', 'voucher_tags'

    def __init__(self, data):
        self.description = data.description
        self.limitations = data.limitations
        self.voucher_types = [entry.type for entry in data.voucher_types] if data.voucher_types else []
        self.voucher_tags = [entry.tag for entry in data.voucher_tags] if data.voucher_tags else []


class VoucherTypeDto(object):
    __slots__ = 'id', 'type'

    def __init__(self, data):
        self.type = data.type


class VoucherTagDto(object):
    __slots__ = 'id', 'tag'

    def __init__(self, data):
        self.tag = data.tag
