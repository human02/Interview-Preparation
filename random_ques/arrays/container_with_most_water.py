"""
You are given an integer array heights where heights[i] represents the height of the ith bar.
You may choose any two bars to form a container. Return the maximum amount of water a container can store.

Example 1:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Example 2:
Input: height = [2,2,2]
Output: 4

Constraints:
2 <= height.length <= 1000
0 <= height[i] <= 1000
"""

# Brute force is to use 2 loops to calculate area of all possible pairs and return max area.
# Optimal approach is to use 2 pointers, one at start and one at end. Calculate area and move the pointer with smaller height towards center.


class Solution:
    def maxWater(self, height):
        n = len(height)
        l = 0
        r = n - 1
        maxArea = 0
        while l < r:
            waterArea = (r - l) * min(height[l], height[r])
            maxArea = max(maxArea, waterArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
