"""

Best Time to Buy and Sell Stock

Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock AT MOST ONCE.

The stock should be purchased before selling it, and both actions cannot occur on the same day.

Examples:
Input: arr = [10, 7, 5, 8, 11, 9]
Output: 6
Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.

Input: arr = [3, 8, 1, 4, 6, 2]
Output: 5

Constraints:
    1 <= n<= 105
    0 <= arr[i] <= 106

"""


class Solution:
    # TC - O(n), SC - O(1)
    def maxProfit(self, prices):
        # Choose first day as selling day initially.
        buy_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - buy_price
            max_profit = max(max_profit, profit)
            # Update sell price if current price is lower than chosen sell price
            if prices[i] < buy_price:
                buy_price = prices[i]
        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit([10, 1, 5, 6, 7, 1]))  # 6
    print(Solution().maxProfit([10, 8, 7, 5, 2]))  # 0
    print(Solution().maxProfit([3, 8, 1, 4, 6, 2]))  # 5
