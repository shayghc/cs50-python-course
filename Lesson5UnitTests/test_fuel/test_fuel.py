from fuel import convert, gauge
import pytest


# Tests for convert function
def test_convert_normal_cases():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75


def test_convert_edge_cases():
    assert convert("99/100") == 99
    assert convert("1/1") == 100
    assert convert("1/100") == 1
    assert convert("0/1") == 0


def test_zero_division_exception():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error_exception():
    with pytest.raises(ValueError):
        convert("5/3")


# Tests for gauge function
def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_empty():
    assert gauge(1) == "E"
    assert gauge(0) == "E"


def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(25) == "25%"
    assert gauge(75) == "75%"
