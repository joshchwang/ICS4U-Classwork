import calc

def test_add():
    assert calc.add(1, 1) == 2
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -2) == -3


def test_subtract():
    assert calc.subtract(2, 1) == 1
    assert calc.subtract(1, 5) == -4
    assert calc.subtract(2, 2) == 0
