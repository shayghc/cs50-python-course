"""
Test suite for the Jar class.

Tests cover the initialization, string representation, deposit, and withdrawal methods of the Jar class.

"""

from jar import Jar
import pytest


def test_init():
    """
    Test the initialization of the Jar object.

    Checks that the capacity of the Jar is set correctly during initialization.

    """
    my_jar = Jar(5)
    assert my_jar.capacity == 5
    my_jar = Jar(10)
    assert my_jar.capacity == 10


def test_str():
    """
    Test the string representation of the Jar object.

    Checks that the string representation of the Jar is correct after depositing cookies.
    Also tests if ValueError is raised when attempting to deposit more cookies than the jar capacity.

    """
    my_jar = Jar()
    assert str(my_jar) == ""
    my_jar.deposit(3)
    assert str(my_jar) == "🍪🍪🍪"
    my_jar.deposit(1)
    assert str(my_jar) == "🍪🍪🍪🍪"
    with pytest.raises(ValueError):
        my_jar.deposit(9)


def test_deposit():
    """
    Test the deposit method of the Jar object.

    Checks that the size attribute of the Jar is updated correctly after depositing cookies.
    Also tests if ValueError is raised when attempting to deposit more cookies than the jar capacity.

    """
    my_jar = Jar()
    my_jar.deposit(5)
    assert my_jar.size == 5
    with pytest.raises(ValueError):
        my_jar.deposit(14)


def test_withdraw():
    """
    Test the withdraw method of the Jar object.

    Checks if ValueError is raised when attempting to withdraw cookies from an empty jar
    and when attempting to withdraw more cookies than the jar contains.

    """
    my_jar = Jar()
    with pytest.raises(ValueError):
        my_jar.withdraw(1)
    with pytest.raises(ValueError):
        my_jar.withdraw(13)