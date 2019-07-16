import pytest

from luupsmap.cli.util.interval_parser import IntervalParser


@pytest.fixture()
def parser():
    return IntervalParser()


def test_empty_entry_should_return_empty(parser):
    interval = parser.parse(' ')

    assert [] == interval


def test_single_entry_with_simple_hours_should_parse(parser):
    interval = parser.parse('Mo-Fr 10-12')[0]

    assert interval['start_day'] == 0
    assert interval['end_day'] == 4
    assert interval['start_hour'] == '10:00'
    assert interval['end_hour'] == '12:00'


def test_single_entry_with_single_day_should_parse(parser):
    interval = parser.parse('Tu 10-12')[0]

    assert interval['start_day'] == 1
    assert interval['end_day'] == 1
    assert interval['start_hour'] == '10:00'
    assert interval['end_hour'] == '12:00'


def test_single_entry_with_midnight_should_parse(parser):
    interval = parser.parse('Tu 10-0')[0]

    assert interval['start_day'] == 1
    assert interval['end_day'] == 1
    assert interval['start_hour'] == '10:00'
    assert interval['end_hour'] == '24:00'


def test_single_entry_with_detailed_hours_should_parse(parser):
    interval = parser.parse('Mo-Fr 10:30-12:45')[0]

    assert interval['start_day'] == 0
    assert interval['end_day'] == 4
    assert interval['start_hour'] == '10:30'
    assert interval['end_hour'] == '12:45'


def test_roll_over_entries_should_parse(parser):
    interval = parser.parse('Mo-Fr 21-04')

    assert len(interval) == 2
    first, second = interval[0], interval[1]
    assert first['end_hour'] == '24:00'
    assert second['start_hour'] == '00:00'
    assert first['start_day'] + 1 == second['start_day']
    assert first['end_day'] + 1 == second['end_day']


def test_multiple_entries_should_parse(parser):
    interval = parser.parse('Mo 10-12, Sa 10-12')

    assert len(interval) == 2


def test_single_entry_with_single_month_should_parse(parser):
    interval = parser.parse('Mo 10-12 Jan')[0]

    assert interval['start_month'] == 1
    assert interval['end_month'] == 1


def test_single_entry_with_months_should_parse(parser):
    interval = parser.parse('Mo 10-12 Jan-Jul')[0]

    assert interval['start_month'] == 1
    assert interval['end_month'] == 7
