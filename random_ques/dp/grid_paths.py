"""
Given two integers m and n, representing the number of rows and columns of a 2d array named matrix.
Return the number of unique ways to go from the top-left cell (matrix[0][0]) to the bottom-right cell (matrix[m-1][n-1]).
Movement is allowed only in two directions from a cell: right and bottom.

Examples:
Input: m = 3, n = 2
Output: 3

Explanation:
There are 3 unique ways to go from the top left to the bottom right cell.
1) right -> down -> down
2) down -> right -> down
3) down -> down -> right


Input: m = 2, n = 4
Output: 4

Input: m = 3, n = 3
Output:6

Constraints:
1 <= n, m <= 100
The answer will not exceed 109
"""


def soln_recur(m, n):
    grid_paths_recur(m - 1, n - 1)


def grid_paths_recur(i, j):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    up = grid_paths_recur(i - 1, j)
    left = grid_paths_recur(i, j - 1)
    return up + left


def soln_memo(m, n):
    dp = [[-1 for j in range(n)] for i in range(m)]
    grid_paths_memo(m - 1, n - 1, dp)


def grid_paths_memo(i, j, dp):
    if i == 0 or j == 0:
        return 1
    if i < 0 or j < 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = grid_paths_memo(i - 1, j)
    left = grid_paths_memo(i, j - 1)
    dp[i][j] = up + left
    return dp[i][j]


def soln_tabu(m, n):
    """Initialize a memoization table (dp)
    to store the results of subproblems"""
    dp = [[0 for _ in range(n)] for _ in range(m)]
    grid_path_tabulation(m, n, dp)


def grid_path_tabulation(m, n, dp):
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = 1
            if i > 1:
                up = dp(i - 1, j)
            if j > 1:
                left = dp(i, j - 1)
            dp[i][j] = up + left
        return dp[m - 1][n - 1]


def grid_path_spaceOP(m, n):
    # Function to solve the problem using space optimization
    """Create a list to represent the previous row of the grid"""
    prev = [0] * n

    # Iterate through the rows of the grid
    for i in range(m):
        """Create a temporary list to represent the current row"""
        temp = [0] * n

        for j in range(n):
            # Base case
            if i == 0 and j == 0:
                temp[j] = 1
                continue

            """ Initialize variables to store the number 
            of ways from the cell above (up) and left (left)"""
            up = prev[j] if i > 0 else 0
            left = temp[j - 1] if j > 0 else 0

            """ Calculate the number of ways to reach 
            the current cell by adding 'up' and 'left'"""
            temp[j] = up + left

        """ Update the previous list with 
        values calculated for the current row"""
        prev = temp

    """ The result is stored in the last
    cell of the previous row (n-1)"""
    return prev[-1]
