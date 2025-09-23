"""
You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc)
and an integer amount representing a target amount of money.

Return the fewest number of coins that you need to make up the exact target amount.
If it is impossible to make up the amount, return -1.

Example 1:
Input: coins = [1,5,10], amount = 12
Output: 3

Example 2:
Input: coins = [2], amount = 3
Output: -1

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4
"""


class Solution:
    def coinChange_recursive(self, coins, amount):
        n = len(coins)

        def helper(i, target):
            if target == 0:
                return 0
            if i == n or target < 0:
                return float("inf")

            pick = 1 + helper(i, target - coins[i])
            not_pick = helper(i + 1, target)

            return min(pick, not_pick)

        ans = helper(0, amount)
        return -1 if ans == float("inf") else ans

    def coinChange_memo(self, coins, amount):
        n = len(coins)
        dp = {}

        def helper(i, target):
            if target == 0:
                return 0
            if i == n or target < 0:
                return float("inf")
            if (i, target) in dp:
                return dp[(i, target)]
            pick = 1 + helper(i, target - coins[i])
            not_pick = helper(i + 1, target)
            dp[(i, target)] = min(pick, not_pick)
            return dp[(i, target)]

        ans = helper(0, amount)
        return -1 if ans == float("inf") else ans

    def coinChange_tab(self, coins, amount):
        n = len(coins)
        dp = [
            [0 if j == 0 else float("inf") for j in range(amount + 1)]
            for i in range(n + 1)
        ]

        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if coins[i - 1] <= j:
                    pick = 1 + dp[i][j - coins[i - 1]]
                    not_pick = dp[i - 1][j]
                    dp[i][j] = min(pick, not_pick)
                else:
                    dp[i][j] = dp[i - 1][j]

        return -1 if dp[n][amount] == float("inf") else dp[n][amount]
