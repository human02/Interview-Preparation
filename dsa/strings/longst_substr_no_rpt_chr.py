"""

Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:
Input: s = "xxxx"
Output: 1

Constraints:
    0 <= s.length <= 1000
    s may consist of printable ASCII characters.

"""


class Solution:
    # TC - O(n), SC - O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Idea:
        - Two Pointer approach:
            - make a map with all the ASCII char and set to -1
            - we store index here for already traversed chars of the string
            - Iterate using l,r starting from 0, increase r:
               - if curr_char is already seen, then update l to max(l,next of prev occureance of r)

        """
        # 256 - All ASCII characters
        mpp = [-1] * 256
        l, r, maxi = 0, 0, 0
        while r < len(s):
            # if s[r] already exists in current window, start from next index of previous index of s[r].
            if mpp[ord(s[r])] != -1:
                # Update l to right of previous index of s[r]
                l = max(mpp[ord(s[r])] + 1, l)

            curr_len = r - l + 1
            maxi = max(maxi, curr_len)
            # most recent position where this character appeared
            mpp[ord(s[r])] = r
            r += 1
        return maxi


if __name__ == "__main__":
    obj = Solution()
    print(obj.lengthOfLongestSubstring("zxyzxyz"))
    print(obj.lengthOfLongestSubstring("xxxx"))
