"""
498. Diagonal Traverse
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105
"""


class Solution:
    def traverse_diag(self, matrix):
        if not matrix:
            return []

        result = []

        rows, cols = len(matrix), len(matrix[0])

        # d = number of diagonals => Total Diagonals = rows+cols-1
        for d in range(rows + cols - 1):
            intermediate = []

            # Calculate starting point for each diagonal
            if d < cols:
                row = 0
                col = d
            else:
                row = d - cols + 1
                col = cols - 1

            # top right to bottom left travesrsal of diagonal
            while r < rows and c >= 0:
                intermediate.append(matrix[r][c])
                r += 1
                c -= 1

            # Reversing for zigzag
            if d % 2 == 0:
                result.extend(intermediate[::-1])
            else:
                result.extend(intermediate)
        return result
