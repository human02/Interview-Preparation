"""
Minimum Path Sum

You are given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which
minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [
                [1,2,0],
                [5,4,2],
                [1,1,3]
              ]
Output: 8
Explanation: The path with minimum sum is 1 -> 2 -> 0 -> 2 -> 3.

Example 2:
Input: grid = [
                [2,2],
                [1,0]
              ]
Output: 3

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    0 <= grid[i][j] <= 200
"""


class Solution:
    # TC - O(2^m+n), SC - O(m+n)
    def min_path_sum_recursive(self, grid):
        m = len(grid)
        n = len(grid[0])

        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i >= m or j >= n:
                return float("inf")

            right = helper(i, j + 1)
            down = helper(i + 1, j)
            return grid[i][j] + min(right, down)

        return helper(0, 0)

    # TC - O(m*n), SC - O(m*n)
    def min_path_memo(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def helper(i, j):
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if i >= m or j >= n:
                return float("inf")
            if dp[i][j] != -1:
                return dp[i][j]

            right = helper(i, j + 1)
            down = helper(i + 1, j)

            dp[i][j] = grid[i][j] + min(right, down)
            return dp[i][j]

        return helper(0, 0)
