"""

Best Time to Buy and Sell Stock - II

Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock ANY NUMBER OF TIMES.

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
    # TC - O(2^n), SC - O(n)
    def stockBuySell_recur(self, arr):
        n = len(arr)

        def helper(ind, buy):

            if ind == n:
                return 0  # no profit even if you hold stocks

            profit = 0

            # able to buy
            if buy == 1:
                # Profit = sell + "- buy"
                # max(not buy today, buy today)
                profit = max(
                    0 + helper(ind + 1, 1),
                    -arr[ind] + helper(ind + 1, 0),
                )

            # able to sell
            else:
                # Profit = "+sell" - buy
                # max(not sell today,sell today)
                profit = max(
                    0 + helper(ind + 1, 0),
                    arr[ind] + helper(ind + 1, 1),
                )
            return profit

        return helper(0, 1)

    # TC - O(n*2), SC - O(n*2) for dp + O(n) for stack
    def stockBuySell_memo(self, arr):
        n = len(arr)
        dp = [[-1] * 2 for _ in range(n)]

        def helper(ind, buy, dp):

            if ind == n:
                return 0  # no profit even if you hold stocks

            if dp[ind][buy] != -1:
                return dp[ind][buy]

            profit = 0

            # able to buy
            if buy == 1:
                # Profit = sell + "- buy"
                # max(not buy today, buy today)
                profit = max(
                    0 + helper(ind + 1, 1, dp),
                    -arr[ind] + helper(ind + 1, 0, dp),
                )

            # able to sell
            else:
                # Profit = "+sell" - buy
                # max(not sell today,sell today)
                profit = max(
                    0 + helper(ind + 1, 0, dp),
                    arr[ind] + helper(ind + 1, 1, dp),
                )
            dp[ind][buy] = profit
            return dp[ind][buy]

        return helper(0, 1, dp)


if __name__ == "__main__":
    obj = Solution()
    print(f"\n Answer = {obj.stockBuySell_recur([10, 7, 5, 8, 11, 9],)}\n")
    print(f"\n Answer = {obj.stockBuySell_memo([10, 7, 5, 8, 11, 9],)}\n")
    print(f"\n Answer = {obj.stockBuySell_recur([5, 4, 3, 2, 1],)}\n")
    print(f"\n Answer = {obj.stockBuySell_memo([5, 4, 3, 2, 1],)}\n")
    print(f"\n Answer = {obj.stockBuySell_recur([3, 8, 1, 4, 6, 2],)}\n")
    print(f"\n Answer = {obj.stockBuySell_memo([3, 8, 1, 4, 6, 2],)}\n")
