from calendar import different_locale, day_name, day_abbr, month_abbr, month_name


class OpeningHourService:
    def __init__(self, opening_hours):
        self.opening_hours = opening_hours

    def get_readable(self):
        self.__merge_intervals()
        entries = []
        for interval in self.opening_hours:
            entries.append(
                {
                    'hours': self.__get_hours(interval),
                    'days': self.__get_days(interval),
                    'months': self.__get_months(interval),
                })
        return entries

    def __merge_intervals(self):
        merged = []
        intervals = self.opening_hours
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
        self.opening_hours = merged

    def __get_days(self, interval):
        start_day = self.__get_day_name(interval.start_day)
        end_day = self.__get_day_name(interval.end_day)
        if start_day == end_day:
            return start_day
        else:
            return '{}-{}'.format(start_day, end_day)

    @staticmethod
    def __get_day_name(day_no, short=False):
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

    @staticmethod
    def __get_hours(interval):
        start_time = interval.start_hour.strftime("%H:%M")
        end_time = interval.end_hour.strftime("%H:%M")

        if end_time == '00:00':
            end_time = '24:00'

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

    @staticmethod
    def __get_month_name(month_no, short=False):
        with different_locale('de_AT.UTF8') as encoding:
            if short:
                s = month_abbr[month_no]
            else:
                s = month_name[month_no]
            if encoding is not None:
                s = s.decode(encoding)
            return s
