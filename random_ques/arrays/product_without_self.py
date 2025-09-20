"""
Given an integer array nums, return an array output where output[i] is the product of all the elements
of nums except nums[i]. Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n) time without using the division operation?

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

"""


class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix, suffix, res = [1] * n, [1] * n, [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        for i in range(n):
            res[i] = prefix[i] * suffix[i]

        return res
