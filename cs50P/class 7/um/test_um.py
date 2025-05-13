from um import count

def test_um():
    assert count("um i am um andre") == 2

def test_yum():
    assert count("yummy lol um yum") == 1

def test_nonwordum():
    assert count("Um, i am, um.") == 2


