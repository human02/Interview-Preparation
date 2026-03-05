"""

Coin Change II

Give an array of coins of n integers representing coin denominations.
Your task is to find the number of distinct combinations that sum up to a specified amount of money.
If it's impossible to achieve the exact amount with any combination of coins, return 0.
Single coin can be used any number of times. Return your answer with modulo 10^9+7.

Example 1:
Input: coins = [2,4,10], amount = 10
Output: 4
Explanation:
    There are four ways to make the amount 10:
    1. 2+2+2+2+2
    2. 2+4+4
    3. 10
    4. 2+2+2+4

Example 2:
Input: coins = [5], amount = 5
Output: 1

Example 3:
Input: coins = [1,2,3,5], amount = 5
Output: 6

Constraints:
    1 <= n, coins[i], amount <= 103
    All the values of coins are unique.

"""


class Solution:
    # TC - O(2^n), SC - O(n)
    def change_recursive(self, coins, amount):
        n = len(coins)

        def helper(ind, target):

            if target == 0:
                return 1  # as finding distinct ways

            if ind == n or target < 0:
                return 0

            pick = helper(ind, target - coins[ind])
            not_pick = helper(ind + 1, target)

            return pick + not_pick  # as finding distinct ways

        return helper(0, amount) % (10**9 + 7)

    # TC - O(n*amount), SC - O(n*amount) + O(n)
    def change_memo(self, coins, amount):
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]

        def helper(ind, target, dp):

            if target == 0:
                return 1

            if ind == n or target < 0:
                return 0

            if dp[ind][target] != -1:
                return dp[ind][target]

            pick = helper(ind, target - coins[ind], dp)
            not_pick = helper(ind + 1, target, dp)

            dp[ind][target] = pick + not_pick
            return dp[ind][target]

        return helper(0, amount, dp) % (10**9 + 7)
if __name__ == "__main__":
    obj = Solution()
    print(obj.change_recursive([2, 4, 10], 10))
    print(obj.change_recursive([5], 5))
    print(obj.change_recursive([1, 2, 3, 5], 5))
