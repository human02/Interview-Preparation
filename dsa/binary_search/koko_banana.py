"""
Koko eating bananas

A monkey is given n piles of bananas, where the 'ith' pile has nums[i] bananas.
An integer h represents the total time in hours to eat all the bananas.
Each hour, the monkey chooses a non-empty pile of bananas and eats k bananas.
If the pile contains fewer than k bananas, the monkey eats all the bananas in that pile and does not consume any more bananas in that hour.
Determine the minimum number of bananas the monkey must eat per hour to finish all the bananas within h hours.


Examples:
Input: n = 4, nums = [7, 15, 6, 3], h = 8
Output: 5
Explanation: If Koko eats 5 bananas/hr, he will take 2, 3, 2, and 1 hour to eat the piles accordingly. So, he will take 8 hours to complete all the piles.

Input: n = 5, nums = [25, 12, 8, 14, 19], h = 5
Output: 25
Explanation: If Koko eats 25 bananas/hr, he will take 1, 1, 1, 1, and 1 hour to eat the piles accordingly. So, he will take 5 hours to complete all the piles.

Input: n = 4, nums = [3, 7, 6, 11], h = 8
Output: 4

Constraints:
  1 <= n <= 104
  n <= h <= 109
  1 <= nums[i] <= 109
"""

import math


# TC - O(max * N), where max is the maximum element in the array and N is the size of the array
# SC - O(1)
class Solution:
    def find_rate(self, nums, h):
        # Idea is to eat within h (lesser works)

        def helper(rate):
            total = 0
            for it in nums:
                total += math.ceil(it / rate)
            return total

        # We can use linear search or binary search.
        low = 1
        high = max(nums)
        rateOfEating = max(nums)

        while low <= high:
            mid = (low + high) // 2
            timeTaken = helper(mid)
            if timeTaken <= h:
                rateOfEating = mid
                high = mid - 1
            else:
                low = mid + 1
        return rateOfEating
