"""

Shortest Path to Get Food

Given an m*n grid where each cell can be one of the following:

* represents your starting position. There is exactly one * cell.
# represents a food location.
O represents an empty space, and you can move through these cells.
X represents an obstacle, and you cannot pass through it.

You can move up, down, left, or right and you must find the shortest path to reach a food cell (#).
If there is no possible path, return -1.

Example 1
Input: grid = [
                ["X","X","X","X","X","X"],
                ["X","*","O","O","O","X"],
                ["X","O","O","#","O","X"],
                ["X","X","X","X","X","X"]
              ]
Output: 3
Explanation: It takes 3 steps to reach the food.

Example 2
Input: grid = [["X","X","X","X","X"],["X","*","X","O","X"],["X","O","X","#","X"],["X","X","X","X","X"]]
Output: -1
Explanation: It is not possible to reach the food.

Example 3:
Input: grid = [
                ["X","X","X","X","X","X","X","X"],
                ["X","*","O","X","O","#","O","X"],
                ["X","O","O","X","O","O","X","X"],
                ["X","O","O","O","O","#","O","X"],
                ["X","X","X","X","X","X","X","X"]
              ]
Output: 6

Constraints
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 200
    grid[row][col] is '', 'X', 'O', or '#'.
    The grid contains exactly one ''.

"""

from collections import deque


class Solution:
    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    # TC - O(m*n), SC - O(m*n)
    def findShortestPath(self, grid):
        """
        Idea:
        - BFS is the way, undirected graph w/o weight or unit weight.
        - BFS will give the shortest path.
        - Step should be tracked in the queue and returned in the end.
        - Make sure to add to queue:
            - when valid index
            - when not visited previously
            - when grid value is not an obstacle
        """
        m = len(grid)
        n = len(grid[0])

        def isValid(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            return True

        vis = [[0] * n for _ in range(m)]
        q = deque()

        # Find the start point and add to queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "*":
                    q.append((i, j, 0))  # (row,col), step
                    vis[i][j] = 1

        while q:
            r, c, step = q.popleft()

            if grid[r][c] == "#":
                return step

            for k in range(4):
                new_r = r + self.delRow[k]
                new_c = c + self.delCol[k]

                # We want to add if its valid, not obstacle and not visited
                if (
                    isValid(new_r, new_c)
                    and not grid[new_r][new_c] == "X"
                    and not vis[new_r][new_c]
                ):
                    q.append((new_r, new_c, step + 1))
                    vis[new_r][new_c] = 1

        return -1


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.findShortestPath(
            [
                ["X", "X", "X", "X", "X", "X"],
                ["X", "*", "O", "O", "O", "X"],
                ["X", "O", "O", "#", "O", "X"],
                ["X", "X", "X", "X", "X", "X"],
            ]
        )
    )
    print(
        obj.findShortestPath(
            [
                ["X", "X", "X", "X", "X"],
                ["X", "*", "X", "O", "X"],
                ["X", "O", "X", "#", "X"],
                ["X", "X", "X", "X", "X"],
            ]
        )
    )

    print(
        obj.findShortestPath(
            [
                ["X", "X", "X", "X", "X", "X", "X", "X"],
                ["X", "*", "O", "X", "O", "#", "O", "X"],
                ["X", "O", "O", "X", "O", "O", "X", "X"],
                ["X", "O", "O", "O", "O", "#", "O", "X"],
                ["X", "X", "X", "X", "X", "X", "X", "X"],
            ]
        )
    )
