"""
Maximum Product Subarray in an Array

Given an integer array nums. Find the subarray with the largest product, and return the product of the elements
present in that subarray. A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
Input: nums = [4, 5, 3, 7, 1, 2]
Output: 840
Explanation: The largest product is given by the whole array itself

Input: nums = [-5, 0, -2]
Output: 0
Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].

Input: nums = [1, -2, 3, 4, -4, -3]
Output: 144

Constraints:
1 <= nums.length <= 104
-10 <= nums[i] <= 10
-109 <= product of any prefix or suffix of nums <= 109
"""
