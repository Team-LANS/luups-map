import pytest

from luupsmap.cli.util.opening_hours_parser import OpeningHoursParser


@pytest.fixture()
def parser():
    return OpeningHoursParser()


def test_single_entry_with_simple_hours_should_parse(parser):
    interval = parser.parse("Mo-Fr 10-12")[0]

    assert interval.start_day == 0
    assert interval.end_day == 4
    assert interval.start_hour == "10:00"
    assert interval.end_hour == "12:00"


def test_single_entry_with_single_day_should_parse(parser):
    interval = parser.parse("Tu 0-0")[0]

    assert interval.start_day == 1
    assert interval.end_day == 1
    assert interval.start_hour == "10:00"
    assert interval.end_hour == "12:00"


def test_single_entry_with_detailed_hours_should_parse(parser):
    interval = parser.parse("Mo-Fr 10:30-12:45")[0]

    assert interval.start_day == 0
    assert interval.end_day == 4
    assert interval.start_hour == "10:30"
    assert interval.end_hour == "12:45"


def test_multiple_entries_should_parse(parser):
    interval = parser.parse("Mo-Fr 10-12, Sa-Su 7-9")

    assert len(interval) == 2
