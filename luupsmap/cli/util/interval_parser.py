import calendar
import time


class IntervalParser:
    DAY_MAPPING = {v[:2]: k for k, v in enumerate(calendar.day_abbr)}

    MONTH_MAPPING = {v: k for k, v in enumerate(calendar.month_abbr)}

    def __init__(self):
        self.DAY_MAPPING.update({'Ft': 8})
        self.parsed = []

    def parse(self, string):
        blocks = [x.strip() for x in string.split(',')]
        for block in blocks:
            parts = [x.strip() for x in block.split(' ')]
            self.__parse_parts(parts)
        return self.parsed

    def __parse_parts(self, parts):
        start_day, end_day = self.__parse_days(parts)

        start_hour, end_hour = self.__parse_hours(parts)

        # TODO: Add variable months, e.g. if opening hours vary during the year
        start_month, end_month = self.__parse_months(parts)

        arguments = {
            'start_day': start_day,
            'end_day': end_day,
            'start_hour': start_hour,
            'end_hour': end_hour,
            'start_month': start_month,
            'end_month': end_month,
        }

        if start_hour > end_hour:
            self.__split_hours(arguments)
        else:
            self.parsed.append(arguments)

    def __parse_days(self, parts):
        days = parts[0]
        day_split = days.split('-')
        start_day = self.DAY_MAPPING[day_split[0]]
        end_day = self.DAY_MAPPING[day_split[1]] if len(day_split) == 2 else start_day
        return start_day, end_day

    def __parse_months(self, parts):
        start_month = 1
        end_month = 12
        if len(parts) == 3:
            months = parts[2]
            month_split = months.split('-')
            start_month = self.MONTH_MAPPING[month_split[0]]
            end_month = self.MONTH_MAPPING[month_split[1]]
        return start_month, end_month

    def __split_hours(self, arguments):
        additional_args = arguments.copy()
        arguments['end_hour'] = '24:00'
        self.parsed.append(arguments)
        additional_args['start_hour'] = '00:00'
        additional_args['start_day'] = arguments['start_day'] + 1
        additional_args['end_day'] = arguments['end_day'] + 1
        self.parsed.append(additional_args)

    def __parse_hours(self, parts):
        hours = parts[1]
        hours_split = hours.split('-')
        start_hour = time.strftime('%H:%M', self.__try_parse_hour(hours_split[0]))
        end_hour = time.strftime('%H:%M', self.__try_parse_hour(hours_split[1]))
        return start_hour, end_hour

    @staticmethod
    def __try_parse_hour(hour):
        try:
            start_hour = time.strptime(hour, "%H")
        except ValueError:
            start_hour = time.strptime(hour, "%H:%M")
        return start_hour
