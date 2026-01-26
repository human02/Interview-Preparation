"""

516. Longest Palindromic Subsequence

Given a string, Find the longest palindromic subsequence length in given string.
A palindrome is a sequence that reads the same backwards as forward.
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
without changing the order of the remaining elements.

Example 1:
Input: s = "eeeme"
Output: 4
Explanation: The longest palindromic subsequence is "eeee", which has a length of 4.

Example 2:
Input: s = "annb"
Output: 2
Explanation: The longest palindromic subsequence is "nn", which has a length of 2.

Example 3:
Input: s = "s"
Output: 1

Constraints:
    1 ≤ s.length ≤ 1000

"""


class Solution:
    """
    Idea: Extension of Longest Common Subsequence problem.
    - Brute way is to find all subsequence, and check which is the longest palindrome.
    - Optimal way:
        - Get the reverse of the original string and find Longest Common Subsequence.
    """

    def findLPS_brute(self, s):
        rev_s = s[::-1]

        def helper(idx1, idx2):
            if idx1 < 0 or idx2 < 0:
                return 0

            if s[idx1] == rev_s[idx2]:
                return 1 + helper(idx1 - 1, idx2 - 1)
            else:
                return max(helper(idx1 - 1, idx2), helper(idx1, idx2 - 1))

        return helper(len(s) - 1, len(s) - 1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.findLPS_brute("eeeme"))
    print(obj.findLPS_brute("annb"))
    print(obj.findLPS_brute("s"))
