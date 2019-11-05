from list_functions import insert_at, insert_sorted


def test_insert_at():
    original = [1, 2, 3, 4]
    expected = [1, 2, 5, 3, 4]
    result = insert_at(original, 5, 2)
    assert result == expected

    original = [1, 2, 3, 4]
    expected = [5, 1, 2, 3, 4]
    result = insert_at(original, 5, 0)
    assert result == expected  

    original = [1, 2, 3, 4]
    expected = [1, 2, 3, 4, 5]
    result = insert_at(original, 5, 4)
    assert result == expected

    original = [1]
    expected = [1, 0, 0, 5]
    result = insert_at(original, 5, 3)
    assert result == expected

def test_insert_sorted():
    original = [1, 2, 3, 4]
    expected = [1, 2, 2, 3, 4]
    result = insert_sorted(original, 2)
    assert result == expected

    # Beginning
    original = [1, 2, 3, 4]
    expected = [0, 1, 2, 3, 4]
    result = insert_sorted(original, 0)
    assert result == expected

    # End
    original = [1, 2, 3, 4]
    expected = [1, 2, 3, 4, 5]
    result = insert_sorted(original, 5)
    assert result == expected
