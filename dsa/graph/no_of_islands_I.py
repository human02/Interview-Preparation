"""

Number of islands

Given a grid of size M x N (M is the number of rows and N is the number of columns in the grid)
consisting of '0's (Water) and ‘1's(Land). Find the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
or diagonally i.e., in all 8 directions.

Example 1:
Input: grid = [ ["1", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "0"],
                ["1", "1", "1", "0", "1"],
                ["0", "0", "0", "1", "1"] ]
Output: 2
Explanation: This grid contains 2 islands. Each '1' represents a piece of land, and the islands are formed
by connecting adjacent lands horizontally or vertically. Despite some islands having a common edge, they are
considered separate islands because there is no land connectivity in any of the eight directions between them.
Therefore, the grid contains 2 islands.

Example 2:
Input: grid = [ ["1", "0", "0", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "1", "0", "1"," 0"] ]
Output: 1

Example 3:
Input: grid = [ ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"] ]
Output: 1

Constraints:
    M == grid.length
    N == grid[i].length
    1 <= M, N <= 300
    grid[i][j] is '0' or '1'.

"""

from collections import deque


# TC - O(m*n), SC - O(m*n)
class Solution:
    def findIslands(self, grid):
        """
        Idea:
        - BFS traversal to the rescue.
        """
        m = len(grid)
        n = len(grid[0])

        def isValid(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return False
            return True

        vis = [[False for _ in range(n)] for _ in range(m)]
        island_count = 0

        def bfs(r, c):
            vis[r][c] = True
            q = deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()

                # Traversingin all 8 directions
                for delRow in range(-1, 2):
                    for delCol in range(-1, 2):
                        newRow = row + delRow
                        newCol = col + delCol
                        if (
                            isValid(newRow, newCol)
                            and not vis[newRow][newCol]
                            and grid[newRow][newCol] == "1"
                        ):
                            q.append((newRow, newCol))
                            vis[newRow][newCol] = True

        # Will have to start BFS from multiple location
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not vis[i][j]:
                    island_count += 1
                    bfs(i, j)
        return island_count


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.findIslands(
            [
                ["1", "1", "1", "0", "1"],
                ["1", "0", "0", "0", "0"],
                ["1", "1", "1", "0", "1"],
                ["0", "0", "0", "1", "1"],
            ]
        )
    )
    print(
        obj.findIslands(
            [
                ["1", "0", "0", "0", "1"],
                ["0", "1", "0", "1", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "1", "0", "1", " 0"],
            ]
        )
    )
    print(
        obj.findIslands(
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ]
        )
    )
