"""

Contains Duplicate

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false

"""


class Solution:
    # TC - O(n), SC - O(n)
    def containsDuplicate_optimal(self, nums):
        hashSet = set(nums)
        if len(hashSet) < len(nums):
            return True
        return False


if __name__ == "__main__":
    obj = Solution()
    print(f"\nAnswer = {obj.containsDuplicate_optimal([1, 2, 3, 3])}\n")
    print(f"\nAnswer = {obj.containsDuplicate_optimal([1, 2, 3, 4])}\n")
