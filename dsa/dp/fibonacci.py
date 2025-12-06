"""

Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
    Given n, calculate F(n).

Examples:
Input : n = 2
Output : 1
Explanation : F(2) = F(1) + F(0) => 1 + 0 => 1.

Input : n = 3
Output : 2
Explanation : F(3) = F(2) + F(1) => 1 + 1 => 2.

Input : n = 6
Output: 8

Constraints:
    0 <= n <= 20

"""


class Solution:
    # TC - O(2^n), SC - O(n)
    def findFibo_recursive(self, n):

        def helper(ind):
            if ind == 0:
                return 0
            if ind == 1:
                return 1
            return helper(ind - 1) + helper(ind - 2)

        return helper(n)

    # TC - O(n), SC - O(n) + O(n) = O(n)
    def findFibo__memo(self, n):
        dp = [-1] * (n + 1)

        def helper(ind, dp):
            if ind == 0:
                return 0
            if ind == 1:
                return 1
            if dp[ind] != -1:
                return dp[ind]

            dp[ind] = helper(ind - 1, dp) + helper(ind - 2, dp)
            return dp[ind]

        return helper(n, dp)

    # TC - O(n), SC - O(n)
    def findFibo_tabu(self, n):
        dp = [-1] * (n + 1)

        dp[0] = 0
        dp[1] = 1

        for ind in range(2, n + 1):
            dp[ind] = dp[ind - 1] + dp[ind - 2]

        return dp[-1]

    # TC - O(n), SC - O(1)
    def findFibo_spaceOP(self, n):

        prev2 = 0
        prev = 1

        for ind in range(2, n + 1):
            curr = prev + prev2
            prev2 = prev
            prev = curr

        return prev


if __name__ == "__main__":
    obj = Solution()
    print(obj.findFibo_recursive(2))
    print(obj.findFibo__memo(2))
    print(obj.findFibo_tabu(2))
    print(obj.findFibo_spaceOP(2))
    print()
    print(obj.findFibo_recursive(3))
    print(obj.findFibo__memo(3))
    print(obj.findFibo_tabu(3))
    print(obj.findFibo_spaceOP(3))
    print()
    print(obj.findFibo_recursive(6))
    print(obj.findFibo__memo(6))
    print(obj.findFibo_tabu(6))
    print(obj.findFibo_spaceOP(6))
