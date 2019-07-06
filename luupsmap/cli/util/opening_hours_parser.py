import calendar
import time

from luupsmap import Interval


class OpeningHoursParser:
    DAY_MAPPING = {v[:2]: k for k, v in enumerate(calendar.day_abbr)}

    MONTH_MAPPING = {v: k for k, v in enumerate(calendar.month_abbr)}

    def __init__(self):
        self.DAY_MAPPING.update({'Ft': 8})
        self.parsed = []

    def parse(self, string):
        blocks = [x.strip() for x in string.split(',')]
        for block in blocks:
            parts = [x.strip() for x in block.split(' ')]
            self.parsed.append(self.__parse_parts(parts))
        return self.parsed

    def __parse_parts(self, parts):
        days = parts[0]

        day_split = days.split('-')
        start_day = self.DAY_MAPPING[day_split[0]]
        end_day = self.DAY_MAPPING[day_split[1]] if len(day_split) == 2 else start_day

        hours = parts[1]
        start_hour, end_hour = self.__parse_hours(hours)

        start_month = 1
        end_month = 12

        # TODO: Add variable months, e.g. if opening hours vary during the year

        arguments = {
            'start_day': start_day,
            'end_day': end_day,
            'start_hour': start_hour,
            'end_hour': end_hour,
            'start_month': start_month,
            'end_month': end_month,

        }
        return Interval(arguments)

    def __parse_hours(self, hours):
        # TODO: Consider hours spilling over to next day
        hours_split = hours.split('-')
        start_hour = time.strftime('%H:%M', self.__try_parse_hour(hours_split[0]))
        end_hour = time.strftime('%H:%M', self.__try_parse_hour(hours_split[1]))
        return [start_hour, end_hour]

    def __try_parse_hour(self, hour):
        try:
            start_hour = time.strptime(hour, "%H")
        except ValueError:
            start_hour = time.strptime(hour, "%H:%M")
        return start_hour
