"""
Valid Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
    s and t doesn't only consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    # TC - O(n+n) = O(n), SC - O(n)
    def isAnagram(self, s: str, t: str) -> bool:
        # not anagram is not same length
        if len(s) != len(t):
            return False

        # Using freq add and subtract method
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        for ch in t:
            freq[ch] = freq.get(ch, 0) - 1
            if freq[ch] < 0:
                return False

        return all(count == 0 for count in freq.values())

    def isAnagram_Counter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


if __name__ == "__main__":
    obj = Solution()
    print(obj.isAnagram("racecar", "carrace"))
    print(obj.isAnagram("jar", "jam"))
    print()
    print(obj.isAnagram_Counter("racecar", "carrace"))
    print(obj.isAnagram_Counter("jar", "jam"))
