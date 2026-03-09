"""

House Robber - II (Circular Arrangmement)

A thief needs to rob money in a street. The houses in the street are arranged in a circular manner.
Therefore the first and the last house are adjacent to each other. The security system in the street
is such that if adjacent houses are robbed, the police will get notified.

Given an array of integers "Arr" which represents money at each house, we need to return the maximum
amount of money that the thief can rob without alerting the police.

Example 1:
Input: money = [2, 1, 4, 9]
Output: 10
Explanation:
    [2, 1, 4, 9] The underlined houses would give the maximum loot.
    Note that we cannot loot the 1st and 4th houses together.

Example 2:
Input: money = [1, 5, 2, 1, 6]
Output: 11
Explanation:
    [1, 5, 2, 1, 6] The underlined houses would give the maximum loot.

Example 3:
Input: money = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses.
The maximum you can rob is nums[1] + nums[4] = 15.

Example 4:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses.
The maximum you can rob is nums[1] = 4.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""
