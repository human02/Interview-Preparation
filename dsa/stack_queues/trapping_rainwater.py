"""
Trapping Rainwater

Given an array of non-negative integers, height representing the elevation of ground.
Calculate the amount of water that can be trapped after rain.


Examples:
Input: height= [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Output: 6
Explanation: As seen from the diagram 1+1+2+1+1=6 unit of water can be trapped

Input: height= [4, 2, 0, 3, 2, 5]
Output: 9
Expalanation: 2+4+1+2=9 unit of water can be trapped

Input: height= [7, 4, 0, 9]
Output:10

Constraints:
  n == height.length
  1 <= n <= 105
  0 <= height[i] <= 105
"""


class Solution:
    def find_trapped_rainwater(self, height):
        n = len(height)
        water = 0
        prefixMax, suffixMax = [0] * n, [0] * n
        prefixMax[0] = height[0]
        suffixMax[n - 1] = height[n - 1]
        for i in range(1, n):
            prefixMax[i] = max(prefixMax[i - 1], height[i])
        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        for i in range(n):
            water += min(prefixMax[i], suffixMax[i]) - height[i]
        return water

if __name__ == "__main__":
    obj = Solution()
    print(obj.find_trapped_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(obj.find_trapped_rainwater([4, 2, 0, 3, 2, 5]))
    print(obj.find_trapped_rainwater([7, 4, 0, 9]))
