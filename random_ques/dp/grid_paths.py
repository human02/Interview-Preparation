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