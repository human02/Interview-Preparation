"""

136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
    1 <= nums.length <= 3 * 104
    -3 * 104 <= nums[i] <= 3 * 104
    Each element in the array appears twice except for one element which appears only once.

"""

from collections import Counter


class Solution:
    # TC - O(n), SC - O(n)
    def findSingleNum_brute(self, nums):
        """
        Idea:
        - Use hastable to store counts of each element
        - Find the index with freq as 1
        """
        freqMpp = Counter(nums)
        for key, val in freqMpp.items():
            if val == 1:
                return key

if __name__ == "__main__":
    obj = Solution()
    print(obj.findSingleNum_brute([2, 2, 1]))
    print(obj.findSingleNum_brute([4, 1, 2, 1, 2]))
    print(obj.findSingleNum_brute([1]))
