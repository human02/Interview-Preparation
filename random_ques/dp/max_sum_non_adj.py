"""
Given an integer array nums of size n. 
Return the maximum sum possible using the elements of nums such that no two elements taken are adjacent in nums.

Example:
Input: nums = [2,1,4,9]
Output: 11   
Constraints:
1 <= n <= 10^5
0 <= nums[i] <= 10^4    
"""

class Solution:
    """ Function to calculate the maximum
    sum of nonAdjacent elements """
    def nonAdjacent(self, nums):
        n = len(nums)
        dp = [0] * n
        
        # Base case
        dp[0] = nums[0]

        # Iterate through the elements of the array
        for i in range(1, n):
            
            """ Calculate maximum value by either picking
            the current element or not picking it"""
            pick = nums[i]
            if i > 1:
                pick += dp[i - 2]
            nonPick = dp[i - 1]

            # Store the maximum value in dp array
            dp[i] = max(pick, nonPick)

        """ The last element of the dp array
        will contain the maximum sum"""
        return dp[-1]