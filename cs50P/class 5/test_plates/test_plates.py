from plates import is_valid

def test_len():
    assert is_valid("AB34567") == False
    assert is_valid("A") == False
def test_alnum():
    assert is_valid("AB.,!") == False
def test_first():
    assert is_valid("A2332") == False
def test_zero():
    assert is_valid("AB0135") == False
def test_alpha_late():
    assert is_valid("AB13AC") == False
def test_right():
    assert is_valid("ABC123") == True


