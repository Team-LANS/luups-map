"""DTOs related to intervals."""

from calendar import different_locale, day_name, day_abbr, month_abbr, month_name


class OpeningHoursDto(object):
    __slots__ = 'id', 'id_location', 'entries'

    def __init__(self, location):
        self.id_location = location.id
        self.entries = self.__create_entries(location.opening_hours)

    def __create_entries(self, intervals):
        entries = []
        intervals = self.__merge_intervals(intervals)
        for interval in intervals:
            entries.append(
                {
                    'hours': self.__get_hours(interval),
                    'days': self.__get_days(interval),
                    'months': self.__get_months(interval),
                })
        return entries

    def __merge_intervals(self, intervals):
        merged = []
        i = 0
        while i < (len(intervals) - 1):
            current_interval = intervals[i]
            next_interval = intervals[i + 1]
            days_match = (current_interval.start_day + 1 == next_interval.start_day) and (
                current_interval.end_day + 1 == next_interval.end_day)
            if days_match:
                current_interval.end_hour = next_interval.end_hour
                merged.append(current_interval)
                i = i + 2
            else:
                merged.append(intervals[i])
                i = i + 1
        if i < (len(intervals)):
            merged.append(intervals[i])
        merged.sort(key=(lambda x: x.start_day))
        return merged

    def __get_days(self, interval):
        start_day = self.__get_day_name(interval.start_day)
        end_day = self.__get_day_name(interval.end_day)
        if start_day == end_day:
            return start_day
        else:
            return '{}-{}'.format(start_day, end_day)

    def __get_day_name(self, day_no, short=False):
        if day_no >= 7:
            return 'Feiertag'
        with different_locale('de_AT.UTF8') as encoding:
            if short:
                s = day_abbr[day_no]
            else:
                s = day_name[day_no]
            if encoding is not None:
                s = s.decode(encoding)
            return s

    def __get_hours(self, interval):
        start_time = interval.start_hour.strftime("%H:%M")
        end_time = interval.end_hour.strftime("%H:%M")
        return '{}-{}'.format(start_time, end_time)

    def __get_months(self, interval):
        if interval.start_month == 1 and interval.end_month == 12:
            return None
        start_month = self.__get_month_name(interval.start_month)
        end_month = self.__get_month_name(interval.end_month)
        if start_month == end_month:
            return '{}'.format(start_month)
        else:
            return '{} - {}'.format(start_month, end_month)

    def __get_month_name(self, month_no, short=False):
        with different_locale('de_AT.UTF8') as encoding:
            if short:
                s = month_abbr[month_no]
            else:
                s = month_name[month_no]
            if encoding is not None:
                s = s.decode(encoding)
            return s
