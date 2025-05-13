from twttr import shorten


def test_lower():
    assert shorten("zlatan") == "zltn"
    assert shorten("iuaosiouaes") == "ss"


def test_capital():
    assert shorten("NissAN") == "NssN"
    assert shorten("IUOESIOUEAS") == "SS"

def test_integer():
    assert shorten("s1234567890") == "s1234567890"

def test_punctoation():
    assert shorten(",.,:´`ola") == ",.,:´`l"



