from typing import List, Dict


# Create a function that takes three float numbers a, b and c.
# The function will return the average of the three numbers.


def float_average(a: float, b: float, c: float) -> float:
    """Finds the average of the three numbers.

    Args:
        a: a float.
        b: a float.
        c: a float.
    Returns:
        The average of the three numbers.
    """
    return (a + b + c) / 3



# Create a function that will count the number of wins or losses
# or ties in a list of game results. The list will consist of any
# number of strings either “W”, “L” or “T” for win, loss, and tie,
# respectively. The function will take the list of game results and
# a specific result, “W”, “L”, or “T” and output the quantity of
# that specific result in the result list. For example, given a
# list of ["W", "W", "L"] and the specific result of “W”, the
# function will output 2, because there are two wins in the list.


def result_count(results: List[str], occurance: str) -> int:
    """Finds the number of occurances of a specific string.

    Args:
        results: a list of floats.
        occurance: a string.
    Returns:
        the amount of times the string occurs within the list.
    """
    count = 0
    for i in results:
        if i == occurance:
            count += 1
    return count



# You discover that the previous function would be better if we
# sorted the results first. Create a function that will take a
# list of results (like above) and sort them into a dictionary.
# The key is the result, the value is the quantity it appears in
# the list. For example, with the list ["W", "W", "L", “T”], the
# resulting dictionary would be {"W": 2, "L": 1, "T": 1}.


def sort_results(results: List[str]) -> Dict:
    """Sorts the results.

    Args:
        results: a list of strings.
    Returns:
        A dictionary with the sorted results.
    """
    occurance = {}
    for result in results:
        if result in occurance.keys():
            occurance[result] += 1
        else:
            occurance[result] = 1
    return occurance



# Write another function exactly like #2 except it takes a sorted
# inventory dictionary like the one created in #3. The function
# will take a sorted game-result dictionary and a specific result,
# “W”, “L”, or “T”. It will return the quantity of the specific
# result in the result list.


def number_of_results(results: Dict, find_result: str) -> int:
    """Finds a specific str in a dictionary.

    Args:
        results: a dictionary with keys set as strings and values
                 as integers.
        find_result: a string.
    Returns:
        An integer representing the amount of times the specific
        string occurs.
    """
    count = 0
    for key, value in results.items():
        if key == find_result:
            count = value
            break
    return count
