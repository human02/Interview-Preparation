"""
Pacific Atlantic Water Flow
You are given a rectangular island heights where heights[r][c] represents the height
above sea level of the cell at coordinate (r, c).The islands borders the Pacific Ocean
from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell
with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans.
Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell.
You may return the answer in any order.

Example 1:
Input: heights = [
  [4,2,7,3,4],
  [7,4,6,4,7],
  [6,3,5,3,6]
]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[0,1]]

"""


class Solution:
    def pacificAtlantic(self, heights):
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, vis, prevheight):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or (r, c) in vis
                or heights[r][c] < prevheight
            ):
                return
            vis.add((r, c))
            for dx, dy in directions:
                dfs(r + dx, c + dy, vis, heights[r][c])

        for i in range(cols):
            dfs(0, i, pac, heights[0][i])
            dfs(rows - 1, i, atl, heights[rows - 1][i])
        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols - 1, atl, heights[i][cols - 1])
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
