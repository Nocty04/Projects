import pytest
from project import get_months, buy_decision, get_statistics
from unittest.mock import MagicMock
import pandas as pd
import math
from freezegun import freeze_time

from datetime import date, timedelta

def test_buy_decision(monkeypatch):

    #Test valid input on the decision with 10 stocks
    inputs = iter(["yes", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = buy_decision(5, 10)
    assert result == 10

    #Test valid input on the decision with no
    inputs = iter(["no"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = buy_decision(5, 10)
    assert result == None

    #Test invalid input on the decision with valid after
    inputs = iter(["yes", "adsasd", "5"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = buy_decision(5, 10)
    assert result == 5


@freeze_time("2025-1-1")
def test_get_months(monkeypatch):
        result = get_months()
        print(result)
        expected_result = [
        '2025-01-31','2024-12-31', '2024-11-30', '2024-10-31',
        '2024-09-30','2024-08-31', '2024-07-31', '2024-06-30',
        '2024-05-31','2024-04-30', '2024-03-31', '2024-02-29',
]

        assert result == expected_result

def test_get_statistics(monkeypatch):
    mock_series = MagicMock() #creates a mock object that is like a panda_series

    mock_series.pct_change.return_value = pd.Series([0.05, -0.02, 0.03]) #changes thhe pct change of the object to the specified pand series

    monkeypatch.setattr(pd, "Series", lambda _: mock_series) #replaces the original series with the mock_series

    m = [100, 105, 103, 106]

    expected_value = 2.0
    deviation = 2.943920288775949

    result = get_statistics(m)
    assert result == (expected_value, deviation)






