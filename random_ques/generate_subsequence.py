"""
Generate Subsequences of a String

Given a string s, return all possible non-empty subsequences of s, sorted in lexicographical order.
A subsequence of a string is a new string generated from the original string with some characters (possibly none)
deleted without changing the relative order of the remaining characters.

Example 1:
Input: s = "ba"
Output: ["a","ab","b"]

Example 2:
Input: s = "xyz"
Output: ["x","xy","xyz","xz","y","yz","z"]

Constraints:
1 <= s.length <= 16
s consists of lowercase English letters.
"""


class Solution:
    def generateSubsequences(self, s):
        n = len(s)
        result = []

        def helper(ind, res):
            if ind == n:
                if len(res):
                    result.append(res)
                return
            # pick
            helper(ind + 1, res + s[ind])
            # not pick
            helper(ind + 1, res)

        helper(0, [])
        return result.sort()
