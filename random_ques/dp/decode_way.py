"""
Decode Ways

A string consisting of uppercase english characters can be encoded to a number using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode a message, digits must be grouped and then mapped back into letters using the reverse of the mapping above.
There may be multiple ways to decode a message. For example, "1012" can be mapped into:
"JAB" with the grouping (10 1 2)
"JL" with the grouping (10 12)

The grouping (1 01 2) is invalid because 01 cannot be mapped into a letter since it contains a leading zero.

Given a string s containing only digits, return the number of ways to decode it.
You can assume that the answer fits in a 32-bit integer.

Example:
Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).


Example 2:
"""


class Solution:
    def max_ways_recursive(self, s):
        n = len(s)

        def helper(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            pick1, pick2 = 0, 0
            pick1 = helper(i + 1)
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                pick2 = helper(i + 2)
            return pick1 + pick2

        return helper(0)

    def max_ways_memo(self, s):
        n = len(s)
        dp = [-1] * n

        def helper(i):
            if dp[i] != -1:
                return dp[i]
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            pick1, pick2 = 0, 0
            pick1 = helper(i + 1)
            if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                pick2 = helper(i + 2)
            dp[i] = pick1 + pick2
            return dp[i]

        return helper(0)

    def max_ways_tab(self, s):
        n = len(s)
        dp = [0] * (n + 1)

        # base case: empty string has 1 way
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] != "0":
                pick1 = dp[i + 1]

                pick2 = 0
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    pick2 = dp[i + 2]

                dp[i] = pick1 + pick2

        return dp[0]

    def max_ways_space_opt(self, s):
        n = len(s)

        # dp[i+1] = next1, dp[i+2] = next2
        prev, prev2 = 1, 0  # dp[n] = 1, dp[n+1] = 0

        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                curr = 0
            else:
                pick1 = prev
                pick2 = 0
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    pick2 = prev2
                curr = pick1 + pick2

            # shift
            next2, next1 = next1, curr

        return next1
