"""

130. Surrounded Regions

You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

    Connect: A cell is connected to adjacent cells horizontally or vertically.

    Region: To form a region connect every 'O' cell.

    Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none
    of the region cells are on the edge of the board.

To capture a surrounded region, replace all 'O's with 'X's in-place within the original board.

Example 1:
Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation:
In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

Example 2:
Input: board = [["X"]]
Output: [["X"]]

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 200
    board[i][j] is 'X' or 'O'.

"""

from collections import deque


class Solution:

    # TC - O(m*n), SC - O(m*n)
    def fill(self, mat):
        """
        Idea:
        - Use BFS to traverse and mark "O" nodes connected with border "0".
        - During these BFS we mark these nodes as visited.
        - At last check if any node is "O" and not visited previously, then mark it as "X".
        """
        m = len(mat)
        n = len(mat[0])
        delRow = [0, 1, 0, -1]
        delCol = [1, 0, -1, 0]
        vis = [[False] * (n) for _ in range(m)]

        def isValid(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            else:
                return True

        def bfs(i, j):

            vis[i][j] = True
            q = deque([(i, j)])

            while q:
                row, col = q.popleft()

                for k in range(4):
                    newRow = row + delRow[k]
                    newCol = col + delCol[k]
                    if (
                        isValid(newRow, newCol)
                        and not vis[newRow][newCol]
                        and mat[newRow][newCol] == "O"
                    ):
                        q.append((newRow, newCol))
                        vis[newRow][newCol] = True

        # first row, last row
        for i in range(n):
            if mat[0][i] == "O":
                bfs(0, i)
            if mat[m - 1][i] == "O":
                bfs(m - 1, i)

        # first col, last col
        for i in range(m):
            if mat[i][0] == "O":
                bfs(i, 0)
            if mat[i][n - 1] == "O":
                bfs(i, n - 1)

        # Flip unvisited "O" to "X"
        for i in range(m):
            for j in range(n):
                if mat[i][j] == "O" and not vis[i][j]:
                    mat[i][j] = "X"

        return mat


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.fill(
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ]
        )
    )
