"""
Longest common subsequence
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

"""


class Solution:
    def lcs_recur(self, str1, str2):
        n1 = len(str1)
        n2 = len(str2)
        return self.helper(n1 - 1, n2 - 1, str1, str2)

    def helper_recur(self, idx1, idx2, s1, s2):
        # Base case:
        if idx1 < 0 or idx2 < 0:
            return 0
        # When characters in both strs are same
        if s1[idx1] == s2[idx2]:
            return 1 + self.helper(idx1 - 1, idx2 - 1, s1, s2)
        # We check both cases by reducing each char in each case
        else:
            return max(
                self.helper(idx1 - 1, idx2, s1, s2), self.helper(idx1, idx2 - 1, s1, s2)
            )

    def lcs_memo(self, str1, str2):
        n = len(str1)
        m = len(str2)

        dp = [[-1] * m for _ in range(n)]
        return self.func(str1, str2, n - 1, m - 1, dp)

    def helper_memo(self, s1, s2, ind1, ind2, dp):
        # Base case
        if ind1 < 0 or ind2 < 0:
            return 0

        """ If the result for this pair of indices
        is already calculated, return it"""
        if dp[ind1][ind2] != -1:
            return dp[ind1][ind2]

        """ If the characters at the current 
        indices match, increment the LCS length"""
        if s1[ind1] == s2[ind2]:
            dp[ind1][ind2] = 1 + self.func(s1, s2, ind1 - 1, ind2 - 1, dp)
        else:
            dp[ind1][ind2] = max(
                self.func(s1, s2, ind1, ind2 - 1, dp),
                self.func(s1, s2, ind1 - 1, ind2, dp),
            )
        return dp[ind1][ind2]
