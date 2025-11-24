"""

Best time to buy and sell stock IV

Given an array, arr, of n integers, where arr[i] represents the price of the stock on an ith day,
determine the maximum profit achievable by completing at most k transactions in total. Holding at
most one share of the stock at any given time is allowed, meaning buying and selling the stock k
times is permitted, but the stock must be sold before buying it again. Buying and selling the stock
on the same day is allowed.

Examples:

Input: arr = [3, 2, 6, 5, 0, 3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6 - 2 = 4.
Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3 - 0 = 3.
Total profit is 4 + 3 = 7.

Input: arr = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0], k = 3
Output: 15
Explanation: Buy on day 1 (price = 1) and sell on day 3 (price = 4), profit = 4 - 1 = 3.
Then buy on day 4 (price = 2) and sell on day 6 (price = 7), profit = 7 - 2 = 5.
Then buy on day 7 (price = 2) and sell on day 9 (price = 9), profit = 9 - 2 = 7.
Total profit is 3 + 5 + 7 = 15.

Input: arr = [1, 3, 2, 8, 4, 9], k = 2
Output: 12

Constraints:
    1 <= n<= 103
    0 <= arr[i] <= 104
    0 <= k <= 100

"""
