from typing import List


numbers = [1, 6, 11, 14]



def binary_insert(insert: int, numbers: List[int]) -> List[int]:
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid - 1] <= insert <= numbers[mid + 1]:
            return numbers.insert(mid, insert)
        elif insert > numbers[mid]:
            start = mid + 1
        else:
            end = mid - 1
        return - 1

def g_binary_insert(numbers: List[int], value: int):
    if len(numbers) == 0:
        return [value]
    
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] == value:
            break
        elif numbers[mid] < value:
            start = mid + 1
        elif numbers[mid] > value:
            end = mid - 1
    
    if numbers[mid] >= value:
        index = mid
    elif numbers[mid] < value:
        index = mid + 1

    numbers.insert(index, value)
    return numbers

def r_binary_insert(numbers, value):
    index = 0
    start = 0
    end = len(numbers) - 1
    while start <= end:
        mid = (start + end) // 2
        if numbers[mid] > value:
            end = mid - 1
            index = mid
        elif numbers[mid] <= value:
            start = mid + 1
            index = start
    
    numbers.insert(index, value)
    return numbers

print(binary_insert(7, numbers))