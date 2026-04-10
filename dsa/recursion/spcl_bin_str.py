"""

761. Special Binary String

Special binary strings are binary strings with the following two properties:
    The number of 0's is equal to the number of 1's.
    Every prefix of the binary string has at least as many 1's as 0's.

You are given a special binary string s. A move consists of choosing two consecutive, non-empty, special substrings of s, and swapping them.
Two strings are consecutive if the last character of the first string is exactly one index before the first character of the second string.
Return the lexicographically largest resulting string possible after applying the mentioned operations on the string.

Example 1:
Input: s = "11011000"
Output: "11100100"
Explanation: The strings "10" [occuring at s[1]] and "1100" [at s[3]] are swapped.
This is the lexicographically largest string possible after some number of swaps.

Example 2:
Input: s = "10"
Output: "10"

Example 3:
Input: s = "111000"
Output: "111000"

Example 4:
Input: s = "101100"
Output: "101100"

Constraints:
    1 <= s.length <= 50
    s[i] is either '0' or '1'.
    s is a special binary string.

"""


class Solution:
    # TC - O(n!), SC - O(n!)
    def findlargestStr_brute(self, s):
        """
        Idea:
        - Generate all permuutation of the input str
        - Check which of them are special binary string
        - Sort the valid ones lexicographically
        """

        def find_special_substrings(strng):
            """
            Find all consecutive pairs of special substrings that can be swapped
            """
            balance = 0
            start = 0
            substrings = []

            for i in range(len(strng)):
                balance += 1 if strng[i] == "1" else -1
                if balance == 0:
                    substrings.append((start, i + 1))
                    start = i + 1

            return substrings
