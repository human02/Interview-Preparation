"""

417. Pacific Atlantic Water Flow

You are given a rectangular island heights where heights[r][c] represents the height
above sea level of the cell at coordinate (r, c).The islands borders the Pacific Ocean
from the top and left sides, and borders the Atlantic Ocean from the bottom and right sides.

Water can flow in four directions (up, down, left, or right) from a cell to a neighboring cell
with height equal or lower. Water can also flow into the ocean from cells adjacent to the ocean.

Find all cells where water can flow from that cell to both the Pacific and Atlantic oceans.
Return it as a 2D list where each element is a list [r, c] representing the row and column of the cell.
You may return the answer in any order.

Example 1:
Input: heights = [[4,2,7,3,4],[7,4,6,4,7],[6,3,5,3,6]]
Output: [[0,2],[0,4],[1,0],[1,1],[1,2],[1,3],[1,4],[2,0]]

Example 2:
Input: heights = [[1],[1]]
Output: [[0,0],[0,1]]

Constraints:
    m == heights.length
    n == heights[r].length
    1 <= m, n <= 200
    0 <= heights[r][c] <= 105

"""


class Solution:

    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    # TC - O(m*n), SC - O(m*n)
    def pacificAtlantic(self, heights):
        """
        Idea:
        - DFS/BFS Traversal from each border side.
        - We track cells visited by either corner in diff vis arr.
        - all 4 boundary cells as starting cells for traverse
        - Add nodes visited by each in respective visited arrays.
        - Ans = common nodes in both the visited sets(PAC/ATL)
        """
        m = len(heights)
        n = len(heights[0])

        def isValid(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True

        # visiting arr for each type
        pac, atl = set(), set()

        def dfs(r, c, vis, prevheight):
            if not isValid(r, c) or (r, c) in vis or heights[r][c] < prevheight:
                return

            vis.add((r, c))

            for i in range(4):
                newRow = r + self.delRow[i]
                newCol = c + self.delCol[i]
                dfs(newRow, newCol, vis, heights[r][c])

        # top row, last row
        for i in range(n):
            dfs(0, i, pac, heights[0][i])  # Pacific
            dfs(m - 1, i, atl, heights[m - 1][i])  # Atlantic

        # first col, last col
        for i in range(m):
            dfs(i, 0, pac, heights[i][0])  # Pacific
            dfs(i, n - 1, atl, heights[i][n - 1])  # Atlantic

        res = []  # store indexes that are in both visited sets
        for i in range(m):
            for j in range(n):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.pacificAtlantic([[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]))
