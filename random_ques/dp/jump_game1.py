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
