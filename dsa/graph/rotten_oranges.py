"""
Rotten Oranges

Given an n x m grid, where each cell has the following values :
2 - represents a rotten orange
1 - represents a Fresh orange
0 - represents an Empty Cell

Every minute, if a fresh orange is adjacent to a rotten orange in 4-direction, it becomes rotten.
Return the minimum number of minutes required such that none of the cells has a Fresh Orange.
If it's not possible, return -1.

Examples:
Input: grid = [ [2, 1, 1] , [0, 1, 1] , [1, 0, 1] ]
Output: -1
Explanation: Orange at (3,0) cannot be rotten.

Input: grid = [ [2,1,1] , [1,1,0] , [0,1,1] ]
Output: 4

Input: grid = [[0,1,2],[0,1,2],[2,1,1]]
Output: 1

Constraints:
  1 <= n, m <= 500
  grid[i][j] == 0 or 1 or 2
"""

from collections import deque


class Solution:
    # right, down, left, up
    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    def isValid(self, i, j, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return False
        return True

    def findTime(self, grid):
        m = len(grid)
        n = len(grid[0])

        time = 0
        rotten_oranges = 0
        total_oranges = 0

        # track every rotten orange for start
        q = deque()

        # Find total Oranges and add rotten orange indexes to Q
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    total_oranges += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        while q:
            k = len(q)
            rotten_oranges += k

            # Perform BFS for current level
            for _ in range(k):
                row, col = q.popleft()

                # Traverse the neighbours
                for i in range(4):
                    newRow = row + self.delRow[i]
                    newCol = col + self.delCol[i]
                    if self.isValid(newRow, newCol, m, n) and grid[newRow][newCol] == 1:
                        grid[newRow][newCol] = 2
                        q.append((newRow, newCol))
            """
            -> Only increment time if there are more oranges to rot in the next level.
            -> Without this check, we'd incorrectly add +1 time after processing the last level
            -> when the queue becomes empty and no more rotting will occur.
            -> Example: If last oranges rot at time=2, queue becomes empty, and we shouldn't
            -> count time=3 since nothing happens then. We only count time between levels,
            -> not after the final level completes.
            """
            if q:
                time += 1
        if total_oranges == rotten_oranges:
            return time
        return -1


if __name__ == "__main__":
    sol = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    ans = sol.findTime(grid)
    if ans != -1:
        print(f"\nAll oranges will rot, by time = {ans}\n")
    else:
        print(f"\nAll Oranges wont rot.\n")
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    ans = sol.findTime(grid)
    if ans != -1:
        print(f"\nAll oranges will rot, by time = {ans}\n")
    else:
        print(f"\nAll Oranges won't rot.\n")
