"""
Find the repeating and missing number

Given an integer array nums of size n containing values from [1, n] and each value appears exactly once in the array,
except for A, which appears twice and B which is missing.

Return the values A and B, as an array of size 2, where A appears in the 0-th index and B in the 1st index.
Note: You are not allowed to modify the original array.


Examples:
Input: nums = [3, 5, 4, 1, 1]
Output: [1, 2]
Explanation: 1 appears two times in the array and 2 is missing from nums

Input: nums = [1, 2, 3, 6, 7, 5, 7]
Output: [7, 4]
Explanation: 7 appears two times in the array and 4 is missing from nums.

Input: nums = [6, 5, 7, 1, 8, 6, 4, 3, 2]
Output: [6, 9]

Constraints:
    n == nums.length
    1 <= n <= 105
    n - 2 elements in nums appear exactly once and are valued between [1, n].
    1 element in nums appears twice, and is valued between [1, n].
"""

