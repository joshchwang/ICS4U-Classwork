import evaluation as e


def test_float_average():
    assert e.float_average(3.11, 2.1, 8) == 4.403333333333333
    assert e.float_average(-2, 3.0, 3.11) == 1.3699999999999999
    assert e.float_average(0, 0, 0) == 0


def test_result_count():
    assert e.result_count(["W", "W", "W", "T", "T", "W", "L", "L"], "W") == 4
    assert e.result_count(["W", "T", "W", "L", "W", "T", "W", "L", "L"], "T") == 2
    assert e.result_count(["W", "W", "L", "W", "T", "T", "W", "L", "L"], "L") == 3


def test_sort_results():
    initial_list = ["W", "L", "T", "L", "T", "T", "W", "W", "T"]
    expected = {"W": 3, "L": 2, "T": 4}
    result = e.sort_results(initial_list)
    assert result == expected

    initial_list = ["T", "W", "L", "L", "W", "L", "W", "W", "T"]
    expected = {"W": 4, "L": 3, "T": 2}
    result = e.sort_results(initial_list)
    assert result == expected


    initial_list = ["T", "T", "T", "T", "T", "T", "T", "T", "T"]
    expected = {"T": 9}
    result = e.sort_results(initial_list)
    assert result == expected


def test_number_of_results():
    initial_dict = {"W": 3, "L": 1, "T": 5}
    assert e.number_of_results(initial_dict, "T") == 5

    initial_dict = {"T": 31, "W": 11, "L": 51}
    assert e.number_of_results(initial_dict, "L") == 51

    initial_dict = {"L": 131, "T": 111, "W": 115}
    assert e.number_of_results(initial_dict, "W") == 115
