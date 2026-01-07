"""

5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.

"""


class Solution:
    # TC - O(n^3), SC - O(1)
    def findPalinSubStr_brute(self, s):
        """
        Idea:
        - Find all Substring and check which of them are palindrome
        - Out of the palindrome strings, return the max length one
        """

        n = len(s)

        def isPalindrome(s1):
            i, j = 0, len(s1) - 1
            while i <= j:
                if s1[i] != s1[j]:
                    return False
                i += 1
                j -= 1

            return True

        result = ""
        max_len = 0

        for i in range(n):
            for j in range(i, n):
                substring = s[i : j + 1]
                if isPalindrome(substring) and len(substring) > max_len:
                    max_len = len(substring)
                    result = substring

        return result

if __name__ == "__main__":
    obj = Solution()
    print(obj.findPalinSubStr_brute("babad"))
    print(obj.findPalinSubStr_brute("cbbd"))
