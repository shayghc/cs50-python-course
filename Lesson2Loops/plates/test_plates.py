# "import plates" does not work
import pytest
from plates import is_valid
from plates import check_plate_length
from plates import first_two_chars_are_letters
from plates import numbers_not_in_middle
from plates import first_digit_not_zero

def test_is_valid():
    # Plate 2-6 chars
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("Seamus") == True
    assert is_valid("SeamusC") == False
    # Letters first two chars
    assert is_valid("50CS") == False
    assert is_valid(".,BB") == False
    assert is_valid("0AB") == False
    assert is_valid("B5B") == False
    assert is_valid("AA") == True


def test_check_plate_length():
    assert check_plate_length("1") == False
    assert check_plate_length("12") == True
    assert check_plate_length("123456") == True
    assert check_plate_length("1234567") == False


def test_first_two_chars_are_letters():
    assert first_two_chars_are_letters("00") == False
    assert first_two_chars_are_letters("0A") == False
    assert first_two_chars_are_letters("A0") == False
    assert first_two_chars_are_letters(".A") == False
    assert first_two_chars_are_letters("A.") == False
    assert first_two_chars_are_letters("..") == False
    assert first_two_chars_are_letters("AA") == None
    assert first_two_chars_are_letters("aa") == None


def numbers_not_in_middle():
    assert numbers_not_in_middle("A0AAAA") == False
    assert numbers_not_in_middle("AA00AA") == False
    assert numbers_not_in_middle("AAAAA0A") == False
    assert numbers_not_in_middle("A0A") == False


def test_first_digit_not_zero():
    assert first_digit_not_zero("A01") == False
    assert first_digit_not_zero("A10") == True