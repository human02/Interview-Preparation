"""

Longest Common Subsequence

Given two strings str1 and str2, find the length of their longest common subsequence.
A subsequence is a sequence that appears in the same relative order but not necessarily
contiguous and a common subsequence of two strings is a subsequence that is common to both strings.

Examples:
Input: str1 = "bdefg", str2 = "bfg"
Output: 3
Explanation: The longest common subsequence is "bfg", which has a length of 3.

Input: str1 = "mnop", str2 = "mnq"
Output: 2
Explanation: The longest common subsequence is "mn", which has a length of 2.

Input: str1 = "abc", str2 = "dafb"
Output: 2

Constraints:
    n = str1.length
    m = str2.length
    1 <= n, m <= 103
    str1 and str2 are in lowercase alphabet

"""


class Solution:
    # TC - O(2^(m+n)), SC - O(m+n)
    def lcs_recur(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)

        def helper(idx1, idx2):
            # Base case
            if idx1 < 0 or idx2 < 0:
                return 0

            # When chars in both strs are same, inc length & both index move
            if str1[idx1] == str2[idx2]:
                return 1 + helper(idx1 - 1, idx2 - 1)

            # We check both cases by reducing each char in each case
            else:
                return max(helper(idx1 - 1, idx2), helper(idx1, idx2 - 1))

        return helper(n1 - 1, n2 - 1)

    # TC - O(m*n), SC - O(m*n) + O(n)
    def lcs_memo(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = [[-1] * n for _ in range(m)]

        def helper(ind1, ind2, dp):
            # Base case
            if ind1 < 0 or ind2 < 0:
                return 0

            if dp[ind1][ind2] != -1:
                return dp[ind1][ind2]

            # When chars in both strs are same, inc length & both index move
            if str1[ind1] == str2[ind2]:
                dp[ind1][ind2] = 1 + helper(ind1 - 1, ind2 - 1, dp)
            else:
                dp[ind1][ind2] = max(
                    helper(ind1, ind2 - 1, dp), helper(ind1 - 1, ind2, dp)
                )
            return dp[ind1][ind2]

        return helper(n - 1, m - 1, dp)

    def lcs_tabu(self, str1, str2):
        n = len(str1)
        m = len(str2)

        # necessary for shifting technique as dp[-1] cannot be used in tabulation
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # Initialize base cases, as any string with empty string has LCS length 0
        for i in range(n + 1):
            dp[i][0] = 0
        for i in range(m + 1):
            dp[0][i] = 0

        # Fill in the DP table to calculate length of LCS
        for ind1 in range(1, n + 1):
            for ind2 in range(1, m + 1):
                # Characters match, increment LCS length
                if str1[ind1 - 1] == str2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[n][m]


if __name__ == "__main__":
    obj = Solution()
    print(obj.lcs_recur("bdefg", "bfg"))
    print(obj.lcs_recur("mnop", "mnq"))
    print(obj.lcs_recur("abc", "dafb"))
    print()
    print(obj.lcs_recur("bdefg", "bfg"))
    print(obj.lcs_recur("mnop", "mnq"))
    print(obj.lcs_recur("abc", "dafb"))
