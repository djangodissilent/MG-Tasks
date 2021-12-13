from random import sample
from two_strings import two_strings

def two_strings_brute(s1, s2):
    """
    Brute force solution.

    time complexity: O(len(s1) * len(s2))
    space complexity: O(1)
    """
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                return "YES"
    return "NO"

def get_random_strings(length1, length2):
    """
    Generate random strings of length s1 and s2.
    """
    s1 = ''.join(sample(list('abcdefghijklmnopqrstuvwxyz'), length1))
    s2 = ''.join(sample(list('abcdefghijklmnopqrstuvwxyz'), length2))
    return s1, s2

def test_two_strings():
    """
    Test two_strings function.
    """
    for _ in range(100):
        s1, s2 = get_random_strings(5, 5)
        assert two_strings(s1, s2) == two_strings_brute(s1, s2)