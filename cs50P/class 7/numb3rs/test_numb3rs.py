from numb3rs import validate

def test_invalid():
    assert validate("255.255.255.255") == True
    assert validate("32.32.64.43") == True


def test_valid():
    assert validate("313213.32.32.32") == False
    assert validate("321321.3234.322323.3223")== False

def test_secondbyte():
    assert validate("32.300.32.32") == False


def test_noninteger():
    assert validate("dassd.??.32.32") == False

