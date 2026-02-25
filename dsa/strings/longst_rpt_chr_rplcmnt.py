"""

Longest Repeating Character Replacement

You are given a string s consisting of only uppercase english characters and an integer k.
You can choose up to k characters of the string and replace them with any other uppercase English character.
After performing at most k replacements, return the length of the longest substring which contains only one
distinct character.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5

Constraints:
    1 <= s.length <= 1000
    0 <= k <= s.length

"""


class Solution:
    # TC - O(26n) = O(n), SC - O(1)
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Idea:
        - at any point, max freq of most occuring element is longest repeating character.
        - Number of changes needed = len(current substr) - maxFreq of the most occurring char.
        - Iterate using two pointers:
            - right moves and we keep calculating curr_max_freq.
            - if len(substr) - curr_max_freq > k:
                - we will reduce substr by moving left and recalculate curr_max_freq.
            - If condition of 'k' is met, we compare it and overwrite maxi.
        - our result is stored in maxi.
        """
        # 256 taken due to ASCII constraint
        mpp = [0] * 26
        # Idea --> changes = len(substr)-maxfreq
        left, right, maxi, curr_max = 0, 0, 0, 0

        while right < len(s):
            mpp[ord(s[right]) - ord("A")] += 1
            curr_max = max(curr_max, mpp[ord(s[right]) - ord("A")])

            # substring reduction by left pointer movement
            while (right - left + 1) - curr_max > k:
                mpp[ord(s[left]) - ord("A")] -= 1
                left += 1

                # recalculate curr_max as window is reduced/can be skipped for optimization
                curr_max = 0
                for i in range(26):
                    curr_max = max(curr_max, mpp[i])

            if (right - left + 1) - curr_max <= k:
                maxi = max(maxi, right - left + 1)
            right += 1
        return maxi


if __name__ == "__main__":
    obj = Solution()
    print(obj.characterReplacement("XYYX", 2))
    print(obj.characterReplacement("AAABABB", 1))
