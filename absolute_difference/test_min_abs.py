import random

from min_abs import min_abs


def quadratic_min_abs(lst):
    """
    Returns the minimum absolute difference in the input list.

    Time Complexity: O(n^2)
    space Complexity: O(1)
    """
    if len(lst) <= 1:
        return 0

    min_diff = float('inf')
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            min_diff = min(min_diff, abs(lst[i] - lst[j]))

    return min_diff


def generate_random_array(n):
    """
    Generates random array of size n.
    """
    return [random.randint(0, n) for _ in range(n)]


def test_min_abs():
    """
    Tests the min_abs function against the brute-force fn.
    """
    for _ in range(100):
        lst = generate_random_array(random.randint(0, 500))
        assert min_abs(lst) == quadratic_min_abs(lst)
