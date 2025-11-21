"""

Jump Game - I

Given an array of integers nums, each element in the array represents the maximum jump length at that position.
Initially starting at the first index of the array, determine if it is possible to reach the last index.
Return true if the last index can be reached, otherwise return false.

Input : [2, 3, 1, 1, 4]
Output : True
Explanation : We can simply take Jump of 1 step at each index to reach the last index.

Input : [3, 2, 1, 0, 4]
Output : False
Explanation : No matter how you make jumps you will always reach the third index (0 base) of the array.
The maximum jump of index three is 0, So you can never reach the last index of array.

Input : [5, 3, 2, 1, 0]
Output : True

Constraints:
    1 <= nums.length <= 104
    0 <= nums[i] <= 105

"""

""" 
We use greedy approach here. 
We want to check at each index, what is the max reachabele index from that particular index.
If at any point we encounter an index that is beyond what we can reach (i > maxReach), 
we cannot proceed further and thus cannot reach the end.
"""


class Solution:
    # TC - O(n), SC - O(1)
    def canJump(self, nums):
        n = len(nums)
        maxReach = 0
        for i in range(n):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + nums[i])
        return True


if __name__ == "__main__":
    obj = Solution()
    print(obj.canJump([2, 3, 1, 1, 4]))
    print(obj.canJump([3, 2, 1, 0, 4]))
    print(obj.canJump([5, 3, 2, 1, 0]))
