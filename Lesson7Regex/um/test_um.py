from um import count


def test_case_insensitve():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1


def test_trailing_chars():
    assert count("Um...") == 1
    assert count("um,") == 1
    assert count("um?") == 1


def test_not_substring():
    assert count("clumsy") == 0
    assert count("alums") == 0
    assert count("album") == 0
    assert count("drums") == 0