from collections import Counter

def two_strings(a, b):
    """
    Given two strings, find the number of common characters between them.
    The matching is case senseistive.

    Approach:
        - Use a hashtable to store the characters of the first string and the second string.
        - Use the python set operation to find if there are common characters.
        - Return the length of the set. (Any overlaping implies a common character)

    time complexity: O(min(len(a), len(b)))
    space complexity: O(max(len(a), len(b)))

    """
    return "YES" if set(a) & set(b) else "NO"
