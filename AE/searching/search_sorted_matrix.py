"""

Sample Input:

    matrix = 
    [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
    ]

    target = 44

Sample Output:
    [3,3]
"""

# O(m*n) time where m and n are dimensions of the matrix| O(1) space
def searchInSortedMatrix_Brute(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])
    res = [-1, -1]
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == target:
                res = [row, column]
    return res


# Optimized
# O(m+n) time as we traverse in such a way| O(1) space
def searchInSortedMatrix(matrix, target):
    # Initialised to reach top right most element
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        # compare from top right and eliminate rows/columns
        if matrix[row][col] > target:
            # values below this element are useless, remove this col
            col -= 1
        elif matrix[row][col] < target:
            # this row is useless, remove it as all value will be lesser
            row += 1
        else:
            return [row, col]
    return [-1, -1]
