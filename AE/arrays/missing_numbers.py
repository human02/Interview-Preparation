"""
    You're given an unordered list of unique integers 'nums' in the
    range [1, n], where n represents the length of nums + 2.
    This means that two numbers in this range are missing from the list.
  
    Write a function that takes in this list and returns a new list with the two
    missing numbers, sorted numerically.

    Sample Input:
        nums = [1, 4, 3]

    Sample Output:
        [2, 5]
"""


def missingNumbers_brute(nums):
    # Finding the n (range)
    n = len(nums)+2

    # Output DS
    result = []

    # Iterating from 1 till range of 'n' inclusive and adding what is not found
    for i in range(1, n+1):
        if i in nums:
            continue
        else:
            result.append(i)
    return result
