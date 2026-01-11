"""

Shortest Distance in a Binary Maze

Given an n x m matrix grid where each cell contains either 0 or 1, determine the shortest distance
between a source cell and a destination cell. You can move to an adjacent cell (up, down, left, or right)
if that adjacent cell has a value of 1. The path can only be created out of cells containing 1.
If the destination cell is not reachable from the source cell, return -1.


Example 1
Input: grid = [[1, 1, 1, 1],[1, 1, 0, 1],[1, 1, 1, 1],[1, 1, 0, 0],[1, 0, 0, 1]], source = [0, 1], destination = [2, 2]
Output: 3
Explanation: The shortest path from (0, 1) to (2, 2) is:
    Move down to (1, 1)
    Move down to (2, 1)
    Move right to (2, 2)
    Thus, the shortest distance is 3

Example 2
Input: grid = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 0],[1, 0, 1, 0, 1]], source = [0, 0], destination = [3, 4]
Output: -1
Explanation: Since, there is no path possible between the source cell and the destination cell, hence we return -1.

Example 2
Input: grid = [[1, 0, 1],[1, 1, 0],[1, 1, 1]], source = [0, 0], destination = [2, 2]
Output: 4

Constraints
    1 ≤ n, m ≤ 500
    grid[i][j] == 0 or grid[i][j] == 1
    The source and destination cells are always inside the given matrix.

"""

from collections import deque


class Solution:
    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    def shortestPath(self, grid, source, destination):
        m = len(grid)
        n = len(grid[0])

        if source == destination:
            return 0

        if grid[source[0]][source[1]] == 0 or grid[destination[0]][destination[1]] == 0:
            return -1

        vis = [[0] * n for _ in range(m)]
        q = deque([(source[0], source[1], 0)])
        vis[source[0]][source[1]] = 1

        while q:
            r, c, dist = q.popleft()

            for i in range(4):
                newR = r + self.delRow[i]
                newC = c + self.delCol[i]

                if (
                    0 <= newR < m
                    and 0 <= newC < n
                    and grid[newR][newC] == 1
                    and not vis[newR][newC]
                ):
                    if newR == destination[0] and newC == destination[1]:
                        return dist + 1

                    q.append((newR, newC, dist + 1))
                    vis[newR][newC] = 1
        return -1


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.shortestPath(
            [[1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1], [1, 1, 0, 0], [1, 0, 0, 1]],
            [0, 0],
            [3, 4],
        )
    )
