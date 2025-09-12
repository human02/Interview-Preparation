"""
A thief needs to rob money in a street. The houses in the street are arranged in a circular manner. 
Therefore the first and the last house are adjacent to each other. The security system in the street 
is such that if adjacent houses are robbed, the police will get notified.

Given an array of integers “Arr'' which represents money at each house, we need to return the maximum 
amount of money that the thief can rob without alerting the police.

Example:
Input: money = [2, 1, 4, 9]
Output: 10
Explanation:
[2, 1, 4, 9] The underlined houses would give the maximum loot.
Note that we cannot loot the 1st and 4th houses together.

Input: money = [1, 5, 2, 1, 6]
Output: 11
Explanation:
[1, 5, 2, 1, 6] The underlined houses would give the maximum loot.
"""

# Similar like max sum with max sum of alternate elements.
def nonAdjacent_spaceOP(self, nums):
    n = len(nums)
    prev, prev2 = nums[0],0
    curr_i = 0
    for i in range(1,n):
        pick=nums[i]
        if i>1:
            pick+=prev2
        notpick = 0+prev
        curr_i = max(pick,notpick)
        prev2 = prev
        prev =curr_i
    return prev

def recur(nums):
    n=len(nums)
    
