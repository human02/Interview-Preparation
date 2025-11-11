"""
3 Sum

Given an integer array nums, return all the triplets:
- [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
One element can be a part of multiple triplets. The output and the triplets can be returned in any order.

Input: nums = [2, -2, 0, 3, -3, 5]
Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
Explanation: nums[1] + nums[2] + nums[0] = 0
nums[4] + nums[1] + nums[5] = 0
nums[4] + nums[2] + nums[3] = 0


Input: nums = [2, -1, -1, 3, -1]
Output: [[-1, -1, 2]]
Explanation: nums[1] + nums[2] + nums[0] = 0
Note that we have used two -1s as they are separate elements with different indexes
But we have not used the -1 at index 4 as that would create a duplicate triplet

Input: nums = [8, -6, 5, 4]
(Give answer with the output and triplets sorted in ascending order)
Output:
[]
"""
