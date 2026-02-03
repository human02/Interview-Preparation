"""

490. The Maze

There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1).
The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop
rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol]
and destination = [destinationrow, destinationcol], return true if the ball can stop at the destination,
otherwise return false.

You may assume that the borders of the maze are all walls.

Example 1:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [4,4]
Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:
Input: maze = [[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]], start = [0,4], destination = [3,2]
Output: false
Explanation: There is no way for the ball to stop at the destination. Notice that you can pass through the destination
but you cannot stop there.

Example 3:
Input: maze = [[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]], start = [4,3], destination = [0,1]
Output: false


Constraints:
    m == maze.length
    n == maze[i].length
    1 <= m, n <= 100
    maze[i][j] is 0 or 1.
    start.length == 2
    destination.length == 2
    0 <= startrow, destinationrow < m
    0 <= startcol, destinationcol < n
    Both the ball and the destination exist in an empty space, and they will not be in the same position initially.
    The maze contains at least 2 empty spaces.

"""

from collections import deque


class Solution:
    delRow = [0, 1, 0, -1]
    delCol = [1, 0, -1, 0]

    # TC - O(m*n(m+n)), SC - O(m*n)
    def ballRollMaze(self, maze, strt, dest):
        """
        Idea:
        - Can use Djikstras - Shortest path with weight
        - BFS is best for unweighted with unit weight

        """
        m = len(maze)
        n = len(maze[0])

        q = deque([strt])

        visit = [[0] * n for _ in range(m)]
        visit[strt[0]][strt[1]] = 1

        while q:
            row, col = q.popleft()
            visit[row][col] = 1

            if row == dest[0] and col == dest[1]:
                return True

            for i in range(4):
                nrow = row + self.delRow[i]
                ncol = col + self.delCol[i]

                # To keep it rolling in the same direction
                while 0 <= nrow < m and 0 <= ncol < n and not maze[nrow][ncol]:
                    nrow += self.delRow[i]
                    ncol += self.delCol[i]

                # retrack to prev coordinates before the wall
                nrow -= self.delRow[i]
                ncol -= self.delCol[i]

                if not visit[nrow][ncol]:
                    visit[nrow][ncol] = 1
                    q.append([nrow, ncol])

        return False


if __name__ == "__main__":
    obj = Solution()
    print(
        obj.ballRollMaze(
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [0, 4],
            [4, 4],
        )
    )
    print(
        obj.ballRollMaze(
            [
                [0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
            ],
            [0, 4],
            [3, 2],
        )
    )
    print(
        obj.ballRollMaze(
            [
                [0, 0, 0, 0, 0],
                [1, 1, 0, 0, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 1, 0, 0, 0],
            ],
            [4, 3],
            [0, 1],
        )
    )
