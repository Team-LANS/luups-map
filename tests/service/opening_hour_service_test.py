import datetime
import time

from luupsmap.model import Interval
from luupsmap.service import OpeningHourService


def test_get_readable_with_empty_hours_should_return_empty():
    result = OpeningHourService([]).get_readable()

    assert result == []


def test_get_readable_with_hours_should_use_hour_format():
    interval = create_interval()
    result = OpeningHourService([interval]).get_readable()

    assert result[0]['hours'] == '10:00-12:00'


def test_get_readable_with_midnight_should_use_hour_format():
    interval = create_interval(end_hour='0')
    result = OpeningHourService([interval]).get_readable()

    assert result[0]['hours'] == '10:00-24:00'


def test_get_readable_with_days_should_print_days_german():
    interval = create_interval()
    result = OpeningHourService([interval]).get_readable()

    assert result[0]['days'] == 'Montag-Sonntag'


def test_get_readable_with_single_day_should_print_day():
    interval = create_interval(start_day=0, end_day=0)
    result = OpeningHourService([interval]).get_readable()

    assert result[0]['days'] == 'Montag'


def test_get_readable_with_holiday_should_print_holiday():
    interval = create_interval(start_day=7, end_day=7)
    result = OpeningHourService([interval]).get_readable()

    assert result[0]['days'] == 'Feiertag'


def test_get_readable_with_time_over_midnight_should_print_proper_interval():
    first = create_interval(start_day=0, end_day=2, start_hour='22', end_hour='00')
    second = create_interval(start_day=1, end_day=3, start_hour='00', end_hour='2')
    result = OpeningHourService([first, second]).get_readable()

    assert result[0]['days'] == 'Montag-Mittwoch'
    assert result[0]['hours'] == '22:00-02:00'


def test_get_readable_with_time_over_midnight_and_more_should_print_proper_interval():
    first = create_interval(start_day=0, end_day=2, start_hour='22', end_hour='00')
    second = create_interval(start_day=1, end_day=3, start_hour='00', end_hour='2')
    third = create_interval(start_day=6, end_day=6)
    result = OpeningHourService([first, second, third]).get_readable()

    assert result[0]['days'] == 'Montag-Mittwoch'
    assert result[0]['hours'] == '22:00-02:00'
    assert result[1]['days'] == 'Sonntag'


def create_interval(start_hour='10',
                    end_hour='12',
                    start_day=0,
                    end_day=6,
                    start_month=1,
                    end_month=12):
    # Workaround to create actual time instead of time_strut
    # See https://stackoverflow.com/a/17767842/2553104
    start_hour = datetime.datetime.fromtimestamp(time.mktime(time.strptime(start_hour, "%H")))
    end_hour = datetime.datetime.fromtimestamp(time.mktime(time.strptime(end_hour, "%H")))
    data = {'start_hour': start_hour,
            'end_hour': end_hour,
            'start_day': start_day,
            'end_day': end_day,
            'start_month': start_month,
            'end_month': end_month
            }
    return Interval(data)
