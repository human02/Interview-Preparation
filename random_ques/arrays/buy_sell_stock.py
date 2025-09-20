"""
Best time to buy and sell stock

Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock at most once.
The stock should be purchased before selling it, and both actions cannot occur on the same day.

Example 1:
Input: arr = [10, 7, 5, 8, 11, 9]
Output: 6
Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

Example 2:
Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.

Input: arr = [3, 8, 1, 4, 6, 2]
Output:5

Constraints:
1 <= n<= 105
0 <= arr[i] <= 106
"""


class Solution:
    def maxProfit(self, arr):
        min_price = arr[0]
        max_profit = 0

        for sell in arr:
            max_profit = max(max_profit, sell - min_price)
            min_price = min(min_price, sell)

        return max_profit
