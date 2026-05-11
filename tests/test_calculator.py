from calculator import add, sub, multiply


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6
