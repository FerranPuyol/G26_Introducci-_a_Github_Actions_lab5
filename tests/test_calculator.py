from calculator import add, sub, multiply

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 5) == 0
