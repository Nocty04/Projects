import pytest
from jar import Jar

def test_init():
    jar = Jar()
    jar._capacity = 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar._size == 0
    jar.deposit(1)
    assert jar._size == 1


def test_withdraw():
    jar = Jar()
    assert jar._size == 0
    jar.deposit(2)
    jar.withdraw(1)
    assert jar._size == 1
