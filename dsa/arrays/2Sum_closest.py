"""

2 Sum - Pair Sum Closest to Target

Given an array arr[] of n integers and an integer target, find a pair of elements from the array such that the sum of the pair is closest to the given target.
Note:
    - Return the pair in sorted order.
    - If multiple pairs have the same closest sum, return the one with the maximum absolute difference (i.e., |a - b| is largest).
    - If no valid pair exists (i.e., array has fewer than 2 elements), return an empty array.

Examples:
Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: Out of all the pairs, [5, 20] has sum = 25 which is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target.

Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.

"""
