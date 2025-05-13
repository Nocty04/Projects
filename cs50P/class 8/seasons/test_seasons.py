import pytest
from seasons import Date

def test_valid():
    dob = Date("2024-09-11")
    today = Date("2024-09-12")
    result = today - dob
    assert str(result) == "one thousand, four hundred forty"

def test_invalid():
    with pytest.raises(SystemExit):
        Date("2000-january-01")

