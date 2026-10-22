from hello import add, subtract


def test_add():
    assert 2 == add(1, 1)


def test_subtract():
    assert 3 == subtract(5, 2)

