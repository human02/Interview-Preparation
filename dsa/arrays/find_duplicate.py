"""

Find the Duplicate Number

You are given an array of integers nums containing n + 1 integers.
Each integer in nums is in the range [1, n] inclusive.

Every integer appears exactly once, except for one integer which appears two or more times.
Return the integer that appears more than once.

Example 1:
Input: nums = [1,2,3,2,2]
Output: 2

Example 2:
Input: nums = [1,2,3,4,4]
Output: 4

Follow-up:
Can you solve the problem without modifying the array nums and using O(1) extra space?

Constraints:
    1 <= n <= 10000
    nums.length == n + 1
    1 <= nums[i] <= n

"""

from collections import Counter


class Solution:
    def findDup_brute(self, nums):
        freq = Counter(nums)
        for key, val in freq.items():
            if val > 1:
                return key


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDup_brute([1, 2, 3, 2, 2]))
    print(obj.findDup_brute([1, 2, 3, 4, 4]))
