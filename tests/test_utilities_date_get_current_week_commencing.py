import pytest
from datetime import datetime, timedelta
from Utilities.Date import get_week_commencing_date  # replace with your actual module

standard_date_format = "%d/%m/%Y"

def test_get_week_commencing_date_with_a_monday_date_string():
    # Test for a date string that is already a Monday
    date = "26/02/2024"  # This is a Monday
    expected = datetime(2024, 2, 26)
    assert get_week_commencing_date(date) == expected.strftime(standard_date_format)

def test_get_week_commencing_date_with_a_friday_date_string():
    # Test for a date string that is not a Monday
    date = "02/02/2024"  # This is a Friday
    expected = datetime(2024, 1, 29)  # The Monday of this week
    assert get_week_commencing_date(date) == expected.strftime(standard_date_format)

def test_get_week_commencing_date_from_previous_month_with_a_wednesday_date_string():
    # Test for a date string that is not a Monday
    date = "01/05/2024"  # This is a Friday
    expected = datetime(2024, 4, 29)  # The Monday of this week
    assert get_week_commencing_date(date) == expected.strftime(standard_date_format)

def test_get_week_commencing_date_with_monday_datetime():
    # Test for a datetime that is already a Monday
    date = datetime(2022, 1, 3)  # This is a Monday
    assert get_week_commencing_date(date) == date.strftime(standard_date_format)

def test_get_week_commencing_date_with_wednesday_datetime():
    # Test for a datetime that is not a Monday
    date = datetime(2022, 1, 5)  # This is a Wednesday
    expected = datetime(2022, 1, 3)  # The Monday of this week
    assert get_week_commencing_date(date) == expected.strftime(standard_date_format)

def test_get_week_commencing_date_with_invalid_numeric():

    # Test for a non-string, non-datetime object
    with pytest.raises(TypeError):
        get_week_commencing_date(123)

def test_get_week_commencing_date_with_invalid_character_string():
    # Test for a non-date string
    with pytest.raises(ValueError):
        get_week_commencing_date("not a date")

def test_get_week_commencing_date_with_invalid_date_string():
    # Test for a non-date string
    with pytest.raises(ValueError):
        get_week_commencing_date("2023-01-10")