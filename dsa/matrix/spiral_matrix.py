"""

54. Spiral Matrix

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 10
    -100 <= matrix[i][j] <= 100

"""


class Solution:
    """
    Idea:
    Use 4 diff loops to print:
        - 1st to print from left to right
        - 2nd to print from top to bottom
        - 3rd to print from right to left
        - 4th to print from bottom to top
    """

    # TC - O(m*n), SC - O(1)
    def spriralTraverse(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        ans = []

        left, top = 0, 0
        right, bottom = n - 1, m - 1

        while left <= right and top <= bottom:

            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # Edge cases - single row and single col cases
            # is there still a bottom row to process?
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # is there still a left row to process?
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.spriralTraverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(obj.spriralTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
