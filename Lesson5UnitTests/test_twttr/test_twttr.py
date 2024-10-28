from twttr import shorten


def test_empty_str():
    assert shorten("") == ""


def test_punctuation():
    assert shorten("Hello!") == "Hll!"
    assert shorten("H--Spam?") == "H--Spm?"
    assert shorten("Good evening, Sir") == "Gd vnng, Sr"


def test_integers():
    assert shorten("1234567890") == "1234567890"


def test_text():
    assert shorten("Hello") == "Hll"
    assert shorten("Twitter") == "Twttr"
    assert shorten("PYTHON") == "PYTHN"
