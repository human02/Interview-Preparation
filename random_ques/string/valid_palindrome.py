"""
Valid Palindrome
Given a string s, return true if it is a palindrome, otherwise return false.
A palindrome is a string that reads the same forward and backward.
It is also case-insensitive and ignores all non-alphanumeric characters.
Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove non-alphanumeric chars, store in lowercase
        s = "".join([c.lower() for c in s if c.isalnum()])

        if len(s) and len(s) < 2:
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    obj = Solution()
    result = obj.isPalindrome(s)
    print(f"\nInput String: {s}")
    print(f"Is Palindrome: {result}\n")
