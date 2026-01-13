"""

Minimize Max Distance to Gas Station

You are given an integer array 'stations' that represents the positions of the gas stations on the x-axis. You are also given an integer k.
You should add k new gas stations. You can add the stations anywhere on the x-axis, and not necessarily on an integer position.

Let penalty() be the maximum distance between adjacent gas stations after adding the k new gas stations.
Find the minimum value of penalty().

Your answer will be accepted if it is within 10**-6 of the true value.

Example 1
Input: n = 10, stations = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10], k = 10
Output: 0.50000
Explanation:
    One of the possible ways to place 10 gas stations is [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10].
    Thus the maximum difference between adjacent gas stations is 0.5.
    Hence, the value of dist is 0.5.
    It can be shown that there is no possible way to add 10 gas stations in such a way that the value of dist is lower than this.

Example 2
Input : n = 10, stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 1
Output: 1.00000
Explanation:
    One of the possible ways to place 1 gas station is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
    New Gas Station is at 11.
    Thus the maximum difference between adjacent gas stations is still 1.
    Hence, the value of dist is 1.
    It can be shown that there is no possible way to add 1 gas station in such a way that the value of dist is lower than this.

Example 3:
Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 9
Output: 0.50000

Example 4:
Input: stations = [23,24,36,39,46,56,57,65,84,98], k = 1
Output: 14.00000

Example 5:
Input: stations= [3, 6, 12, 19, 33, 44, 67, 72, 89, 95], k = 2
Output:

Constraints
    10 <= n <= 5000
    0 <= arr[i] <= 10**9
    stations is sorted in a strictly increasing order
    0 <= k <= 10**6

"""
