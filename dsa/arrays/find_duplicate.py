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
    # TC - O(), SC - O()
    def findDup_brute(self, nums):
        freq = Counter(nums)
        for key, val in freq.items():
            if val > 1:
                return key

    # TC - O(), SC - O()
    def findDup_optimal(self, nums):
        """
        Cycle detection from LL used here
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow


if __name__ == "__main__":
    obj = Solution()
    print(obj.findDup_brute([1, 2, 3, 2, 2]))
    print(obj.findDup_brute([1, 2, 3, 4, 4]))
    print()
    print(obj.findDup_optimal([1, 2, 3, 2, 2]))
    print(obj.findDup_optimal([1, 2, 3, 4, 4]))
