"""

Search in rotated sorted array-I

Given an integer array nums, sorted in ascending order (with distinct values) and a target value k.
The array is rotated at some pivot point that is unknown. Find the index at which k is present and
if k is not present return -1.

Examples:
Input : nums = [4, 5, 6, 7, 0, 1, 2], k = 0
Output: 4
Explanation: Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 3
Output: -1
Explanation: Here, the target is 3. Since 3 is not present in the given rotated sorted array. Thus, we get the output as -1.

Input: nums = [4, 5, 6, 7, 0, 1, 2], k = 5
Output: 1

Constraints:
  1 <= nums.length <= 104
  -104 <= nums[i] <= 104
  All values of nums are unique.
  nums is an ascending array that is possibly rotated.
  -104 <= k <= 104

"""


class Solution:
    # TC - O(logn), SC - O(1)
    def findElement(self, nums, target):
        """
        Idea:
        - The idea is that even rotated, 1 part will be sorted.
        - Use it, to eliminate the part and check other parts.
        """

        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2

            # Return when element found
            if nums[mid] == target:
                return mid

            # Check if left part is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Else, right part is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
