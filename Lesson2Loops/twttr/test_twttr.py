from twttr import shorten

# Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:

def test_empty_str():
    assert shorten("") == ""

def test_punctuation():
    assert(",.!;") == ",.!;"

def test_integers():
    assert shorten("1234567890") == "1234567890"

def test_text():
    assert shorten("Hello") == "Hll"
    assert shorten("Twitter") == "Twttr"
    assert shorten("PYTHON") == "PYTHN"