"""
Jump Game - I

Given an array of integers nums, each element in the array represents the maximum jump length at that position.
Initially starting at the first index of the array, determine if it is possible to reach the last index.
Return true if the last index can be reached, otherwise return false.

Input : [2, 3, 1, 1, 4]
Output : true
Explanation : We can simply take Jump of 1 step at each index to reach the last index.

Input : [3, 2, 1, 0, 4]
Output : false
Explanation : No matter how you make jumps you will always reach the third index (0 base) of the array.
The maximum jump of index three is 0, So you can never reach the last index of array.

Input : [5, 3, 2, 1, 0]
Output : true

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


# We can use greedy approach here. We want to check at each index that what is the max reachabele index.
# If at any index the max reachable index is less than or equal to that index, we cannot reach the end.
def canJump(nums):
    n = len(nums)
    maxReach = 0
    for i in range(n):
        if i > maxReach:
            return False
        maxReach = max(maxReach, i + nums[i])
    return True


assert canJump([2, 3, 1, 1, 4]) == True
assert canJump([3, 2, 1, 0, 4]) == False

