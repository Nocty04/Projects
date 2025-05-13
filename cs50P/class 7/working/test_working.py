import pytest
from working import convert

def test_format():
    with pytest.raises(ValueError):
        convert("9:00 AM 10:00 PM")

def test_invalidhours():
    with pytest.raises(ValueError):
        convert("11:00 AM to 25:00 PM")

def test_dayshift():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 AM to 7:59 PM") == "10:30 to 19:59"

def test_nightshift():
    assert convert("9:00 PM to 5 AM") == "21:00 to 05:00"
    assert convert("10:10 PM to 7:20 AM") == "22:10 to 07:20"


