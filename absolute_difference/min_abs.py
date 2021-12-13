def min_abs(lst):
    """
    Returns the minimum absolute difference between any two numbers in a list.


    Approach:
        - Sort the list to get the following invariant -> { list[i] - lst[i-1] <= list[i - k] for k in [0, len(lst)[ }.
        - Iterate over the list and keep track of the minimum absolute difference.
        - The minimum is the minimum absolute difference between any two numbers in the list.

    time Complexity: O(nlgn)
    space Complexity: O(1)

    Mutates the input list.
    """

    if len(lst) <= 1:
        return 0

    lst.sort()
    min_diff = float('inf')

    for i in range(1, len(lst)):
        min_diff = min(min_diff, abs(lst[i] - lst[i-1]))

    return min_diff


if __name__ == "__main__":
    _ = input()
    lst = list(map(int, input().split()))
    print(min_abs(lst))
