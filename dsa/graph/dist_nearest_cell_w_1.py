"""

Distance of nearest cell having one

Given a binary grid of N x M. Find the distance of the nearest 1 in the grid for each cell.
The distance is calculated as |i1 - i2| + |j1 - j2|, where i1, j1 are the row number and
column number of the current cell, and i2, j2 are the row number and column number of
the nearest cell having value 1.


Example 1
Input: grid = [ [0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1] ]
Output: [ [1, 0, 0, 1], [0, 0, 1, 1], [1, 1, 0, 0] ]
Explanation: 0's at (0,0), (0,3), (1,2), (1,3), (2,0) and (2,1) are at a distance of 1
    from 1's at (0,1),(0,2), (0,2), (2,3), (1,0) and (1,1) respectively.

Example 2
Input: grid = [ [1, 0, 1], [1, 1, 0], [1, 0, 0] ]
Output: [ [0, 1, 0], [0, 0, 1], [0, 1, 2] ]
Explanation: 0's at (0,1), (1,2), (2,1) and (2,2) are at a distance of 1, 1, 1 and 2
    from 1's at (0,0),(0,2), (2,0) and (1,1) respectively.

Example 3
Input : grid = [ [0, 1], [1, 0] ]
Output:[ [1, 0], [0, 1] ]

Constraints
    1 <= N, M <= 500
    grid[i][j] == 0 or 1
    There is atleast one 1 in the grid

"""

from collections import deque


class Solution:
    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    # TC - O(m*n), SC - O(m*n)
    def findNearest(self, grid):
        """
        Idea:
        - BFS ensures that the 1st time we reach a cell, its via the shortest path.
        - Multi-Source BFS needed here.
        - We start from all locations of 1s in the grid.
        - As per the question, only 4 way movement allowed.

        """
        m = len(grid)
        n = len(grid[0])

        def isValid(r, c):
            if r < 0 or c < 0 or r >= m or c >= n:
                return False
            return True

        q = deque()
        # Multi Source BFS

        vis = [[0] * n for _ in range(m)]

        # For storing distance from closest 1
        dist = [[0] * n for _ in range(m)]

        # Start traversals from 1s
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] == 1:
                    q.append(((i, j), 0))  # ((row,col),distance)
                    vis[i][j] = 1

        # BFS
        while q:
            topVals = q.popleft()
            row, col = topVals[0]
            step_dist = topVals[1]

            # update the distance matrix
            dist[row][col] = step_dist

            for i in range(4):
                newR = row + self.delRow[i]
                newC = col + self.delCol[i]

                if isValid(newR, newC) and not vis[newR][newC]:
                    vis[newR][newC] = 1
                    q.append(((newR, newC), step_dist + 1))

        return dist


if __name__ == "__main__":
    obj = Solution()
    print(obj.findNearest([[0, 1, 1, 0], [1, 1, 0, 0], [0, 0, 1, 1]]))
    print(obj.findNearest([[1, 0, 1], [1, 1, 0], [1, 0, 0]]))
    print(obj.findNearest([[0, 1], [1, 0]]))
