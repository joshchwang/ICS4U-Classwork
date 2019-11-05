from typing import List


def insert_at(original: List,
              value: int,
              target_index: int) -> List:
    
    new_list = [0] * (len(original) + 1)
    # Copy up to target_index
    i  = 0
    while i < target_index:
        new_list[i] = original[i]
        i += 1

    # Insert
    new_list[i] = value
    i += 1

    # Copy from target + 1 to the end
    while i < len(new_list):
        new_list[i] = original[i - 1]
        i += 1
    
    return new_list

    # return original[:target_index] + [value] + original[target_index:]


def insert_sorted(original: List, value: int) -> List:
    i = 0
    while i < len(original):
        if original[i] > value:
            break
        i += 1

    return insert_at(original, value, i)
