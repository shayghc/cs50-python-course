from bank import value


def test_zero_return():
    assert value("hello") == 0
    assert value("hello there") == 0
    assert value("hellonearth") == 0
    assert value("HELLO") == 0
    assert value("HeLLo") == 0


def test_ten_return():
    assert value("hell") == 20
    assert value("hello") == 0
    assert value("hi") == 20
    assert value("h") == 20
    assert value("hI") == 20
    assert value("H") == 20


def test_onehundred_return():
    assert value("") == 100
    assert value("Good day!") == 100
    assert value("...") == 100
    assert value("GREETINGS") == 100
