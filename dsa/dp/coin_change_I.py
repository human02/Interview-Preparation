"""

Coin Change - I

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
    # TC - Exponential O(2^n), SC - O(n)
    def coinChange_recursive(self, coins, amount):
        n = len(coins)

        def helper(i, target):
            if target == 0:
                return 0

            # cant be target!=0 as target value needs to keep changing until its <= 0
            if i == n or target < 0:
                return float("inf")  # returning -1 messes the result

            pick = 1 + helper(i, target - coins[i])
            not_pick = helper(i + 1, target)

            return min(pick, not_pick)

        ans = helper(0, amount)
        return -1 if ans == float("inf") else ans

    # TC - O(n*amount), SC - O(n*amount) + O(n)
    def coinChange_memo(self, coins, amount):
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def helper(i, target):
            if target == 0:
                return 0

            if i == n or target < 0:
                return float("inf")

            if dp[i][target] != -1:
                return dp[i][target]

            pick = 1 + helper(i, target - coins[i])
            not_pick = helper(i + 1, target)

            dp[i][target] = min(pick, not_pick)

            return dp[i][target]

        ans = helper(0, amount)
        return -1 if ans == float("inf") else ans
if __name__ == "__main__":
    obj = Solution()
    print(obj.coinChange_recursive([1, 5, 10], 12))
    print(obj.coinChange_recursive([2], 3))
    print()
    print(obj.coinChange_memo([1, 5, 10], 12))
    print(obj.coinChange_memo([2], 3))
