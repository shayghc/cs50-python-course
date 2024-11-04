import pytest
from working import convert


def test_import_convert():
    from working import convert  # Attempt to import convert

    assert callable(convert)  # Check that convert is callable


def test_valid_format():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("8:00 PM to 8:00 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"


def test_invalid_format():
    # Test for invalid format with '-' separator
    with pytest.raises(ValueError):
        convert("8:60 AM - 4:60 PM")
    # Test for invalid format with no time separator
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    # Test for invalid AM/PM range
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("9 AM to 5PM")
    with pytest.raises(ValueError):
        convert("10:7 AM - 5:1 PM")


def test_hours_range():
    # Test for out of range hours
    with pytest.raises(ValueError):
        convert("13 AM to 7 PM")
    with pytest.raises(ValueError):
        convert("9 AM to 14 PM")


def test_minutes_range():
    # Test for out of range minutes
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("9:00 AM to 4:75 PM")
