"""

Top K Frequent Elements

Given an integer array nums and an integer k, return any order list of the k most frequent elements in nums.
Your solution must run in better than O(n log n) time, where n = nums.length.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears once.
       The two most-frequent elements are 1 and 2.

Input: nums = [4,4,6,6,7], k = 2
Output: [4,6]
Explanation: 4 and 6 both occur twice (highest), 7 occurs once.

Input: nums = [-1,-1,-2,-2,-2,-3], k = 1
Output: [-2]

Constraints:
    1 ≤ nums.length ≤ 105
    -104 ≤ nums[i] ≤ 104
    1 ≤ k ≤ number of distinct elements in nums
    The answer is guaranteed to be unique.

"""
