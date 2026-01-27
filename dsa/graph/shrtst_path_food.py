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
