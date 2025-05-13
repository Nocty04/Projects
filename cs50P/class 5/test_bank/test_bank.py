from bank import value

def test_h():
    assert value("hihi") == 20
def test_hello():
    assert value("hello") == 0
def test_case():
    assert value("HELLO") == 0
def test_else():
    assert value("ehewe") == 100
    assert value("dsadsasd") == 100
def test_integer():
    assert value("321") == 100
def test_punctuation():
    assert value("´:;.,") == 100
