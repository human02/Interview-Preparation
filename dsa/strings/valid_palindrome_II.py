"""

680. Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
Input: s = "aba"
Output: true

Example 2:
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:
Input: s = "abc"
Output: false

Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.

"""

if __name__ == "__main__":
    obj = Solution()
    print(obj.isPalindrome("A man, a plan, a canal: Panama"))
    print(obj.isPalindrome("race a car"))
    print(obj.isPalindrome(" "))
