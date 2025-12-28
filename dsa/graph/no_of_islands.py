"""

Number of islands

Given a grid of size M x N (M is the number of rows and N is the number of columns in the grid)
consisting of '0's (Water) and ‘1's(Land). Find the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
or diagonally i.e., in all 8 directions.

Examples:
Input: grid = [ ["1", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "0"],
                ["1", "1", "1", "0", "1"],
                ["0", "0", "0", "1", "1"] ]
Output: 2
Explanation: This grid contains 2 islands. Each '1' represents a piece of land, and the islands are formed
by connecting adjacent lands horizontally or vertically. Despite some islands having a common edge, they are
considered separate islands because there is no land connectivity in any of the eight directions between them.
Therefore, the grid contains 2 islands.

Input: grid = [ ["1", "0", "0", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "1", "0", "1"," 0"] ]
Output: 1
Explanation: In the given grid, there's only one island as all the '1's are connected either horizontally,
vertically, or diagonally, forming a single contiguous landmass surrounded by water on all sides.

Input: grid = [ ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"] ]
Output: 1

Constraints:
    ·  M == grid.length
    ·  N == grid[i].length
    ·  1 <= M, N <= 300
    ·  grid[i][j] is '0' or '1'.

"""

from collections import deque


# TC - O(m*n), SC - O(m*n)
class Solution:
    def findIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    island_count += 1
                    self.bfs(grid, visited, i, j)
        return island_count

    def isValid(self, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True

    def bfs(self, grid, vis, r, c):
        vis[r][c] = True
        q = deque()
        q.append((r, c))
        m = len(grid)
        n = len(grid[0])

        while q:
            row, col = q.popleft()

            # Traversingin all 8 directions
            for delRow in range(-1, 2):
                for delCol in range(-1, 2):
                    newRow = row + delRow
                    newCol = col + delCol
                    if (
                        self.isValid(newRow, newCol, m, n)
                        and not vis[newRow][newCol]
                        and grid[newRow][newCol] == "1"
                    ):
                        q.append((newRow, newCol))
                        vis[newRow][newCol] = True
        return


if __name__ == "__main__":
    grid = [
        ["1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "1", "0", "1"],
        ["0", "0", "0", "1", "1"],
    ]

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to find the number of islands in given grid
    ans = sol.findIslands(grid)

    print(f"\nThe total islands in given grids are {ans}\n")
