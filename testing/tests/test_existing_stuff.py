import math


# test sum(numbers: List[float]) -> float
def test_sum():
    assert sum([]) == 0
    assert sum([1, 1, 1]) == 3
    assert sum([1] * 10000) == 10000

# test math.ceil(float) -> int
def test_ceil():
    assert math.ceil(6.9999999) == 7

# test math.floor(float) -> int
# test f strings
def test_f_strings():
    a = 5
    assert f"hello {a}" == "hello 5"
# test .format()