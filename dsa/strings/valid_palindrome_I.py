"""

125. Valid Palindrome

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

Example 3:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 4:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 5:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("Was it a car or a cat I saw?"))
    print(obj.isPalindrome("tab a cat"))
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    print(obj.isPalindrome("race a car"))
    print(obj.isPalindrome(" "))
