from plates import is_valid


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
    assert is_valid("M") == False
    assert is_valid("MM") == True
    assert is_valid("MM3456") == True
    assert is_valid("ABCDEFG") == False


def test_first_two_chars_are_letters():
    assert is_valid("11") == False
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid(".A") == False
    assert is_valid("A.") == False
    assert is_valid("..") == False
    assert is_valid("AA") == True
    assert is_valid("aa") == True


def test_numbers_not_in_middle():
    assert is_valid("AAAA1A") == False
    assert is_valid("AA11AA") == False
    assert is_valid("AAA111") == True
    assert is_valid("AA1A") == False
    assert is_valid("AA01") == False
    assert is_valid("AA10") == True


def test_no_punctuation():
    assert is_valid("AAAAAA") == True
    assert is_valid("AAA111") == True
    assert is_valid("A.AAAA") == False
    assert is_valid("AAA!AA") == False
    assert is_valid("AAAA:A") == False
