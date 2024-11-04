# "import plates" does not work
import pytest
from plates import is_valid
from plates import check_plate_length
from plates import first_two_chars_are_letters
from plates import numbers_not_in_middle
from plates import no_punctuation

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
    assert first_two_chars_are_letters("11") == False
    assert first_two_chars_are_letters("1A") == False
    assert first_two_chars_are_letters("A1") == False
    assert first_two_chars_are_letters(".A") == False
    assert first_two_chars_are_letters("A.") == False
    assert first_two_chars_are_letters("..") == False
    assert first_two_chars_are_letters("AA") == True
    assert first_two_chars_are_letters("aa") == True


def test_numbers_not_in_middle():
    assert numbers_not_in_middle("AAAA1A") == False
    assert numbers_not_in_middle("AA11AA") == False
    assert numbers_not_in_middle("AAA111") == True
    assert numbers_not_in_middle("AA1A") == False
    assert numbers_not_in_middle("AA01") == False
    assert numbers_not_in_middle("AA10") == True
    
def test_no_punctuation():
    assert no_punctuation("AAAAAA") == True
    assert no_punctuation("AAA111") == True
    assert no_punctuation("A.AAAA") == False
    assert no_punctuation("AAA!AA") == False
    assert no_punctuation("AAAA:A") == False