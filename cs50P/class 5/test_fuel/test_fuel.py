from fuel import convert
from fuel import gauge
import pytest

def test_noninteger():
    with pytest.raises(ValueError):
        convert("y/y")
        convert("!/1")
        convert("/")

def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_tomuch():
    with pytest.raises(ValueError):
        convert("10/2")

def test_fraction():
    assert convert("1/2") == 50

def test_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
def test_full():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
def test_half():
    assert gauge(50) == "50%"


