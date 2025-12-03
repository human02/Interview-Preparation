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
    # TC - O(n), SC - O(n)
    def find_trapped_rainwater(self, height):
        n = len(height)
        water = 0
        prefixMax, suffixMax = [0] * n, [0] * n

        prefixMax[0] = height[0]
        for i in range(1, n):  # O(n)
            prefixMax[i] = max(prefixMax[i - 1], height[i])

        suffixMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):  # O(n)
            suffixMax[i] = max(suffixMax[i + 1], height[i])

        for i in range(n):  # O(n)
            water += min(prefixMax[i], suffixMax[i]) - height[i]
        return water

    # TC - O(n), SC - O(1)
    def find_trapped_rainwater_optimal(self, height):
        n = len(height)
        l, r = 0, n - 1

        leftMax, rightMax = -1, -1

        water = 0
        while l < r:
            if height[l] < height[r]:
                if leftMax > height[l]:
                    water += leftMax - height[l]
                else:
                    leftMax = height[l]
                l += 1
            else:
                if rightMax > height[r]:
                    water += rightMax - height[r]
                else:
                    rightMax = height[r]
                r -= 1
        return water


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_trapped_rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(obj.find_trapped_rainwater([4, 2, 0, 3, 2, 5]))
    print(obj.find_trapped_rainwater([7, 4, 0, 9]))
    print(f"{"-"*20}")
    print(obj.find_trapped_rainwater_optimal([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(obj.find_trapped_rainwater_optimal([4, 2, 0, 3, 2, 5]))
    print(obj.find_trapped_rainwater_optimal([7, 4, 0, 9]))
