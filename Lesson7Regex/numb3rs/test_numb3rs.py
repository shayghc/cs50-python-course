from numb3rs import validate


def test_empty_string():
    assert validate("") == False

def test_whitespace_removed():
    assert validate("  255.100.99.5") == False
    assert validate("  255.100.99.5") == False
    assert validate("255.100.99.5") == True

def test_delimiter():
    assert validate("123,123,123,123") == False
    assert validate("123 123 123 123") == False
    assert validate("123.123.123.123") == True

def test_non_alpha():
    assert validate("cat.123.123.123") == False
    assert validate("123.cat.123.123") == False
    assert validate("123.123.cat.123") == False
    assert validate("123.123.123.cat") == False

def test_octet_range():
    assert validate("256.0.0.0") == False
    assert validate("0.256.0.0") == False
    assert validate("0.0.256.0") == False
    assert validate("0.0.0.256") == False
    assert validate("-1.0.0.0") == False
    assert validate("0.-1.0.0") == False
    assert validate("0.0.-1.0") == False
    assert validate("0.0.0.-1") == False

def test_four_digits():
    assert validate("1234.1.1.1") == False
    assert validate("1.1234.1.1") == False
    assert validate("1.1.1234.1") == False
    assert validate("1.1.1.1234") == False

def test_four_octets():
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False