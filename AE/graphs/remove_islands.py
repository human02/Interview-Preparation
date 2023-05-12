"""
"""

# Trivial solution - traverse all elements (w*h) and do dfs when find 1, mark them in aux ds(initailly set to false).
# THen finally traverse again and check if aux ds value is not set when 1 is found and change it
# O(w*h) time | O(w*h) space


# better soln - only traverse 1st col,row and last col,row and dfs when find 1 and save result in aux ds
# next only traverse the inner matrix (not traverse in first time)
# when you see 1, check if this index not in aux ds, then change to 0 else skip

# O(w*h) time | O(w*h) space
def removeIslands1(matrix):
    # aux ds to store border connected 1s
    onesConnectedToBorder = [[False for col in matrix[0]]for row in matrix]

    # find border+connected 1s
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            rowIsBorder = row == 0 or row == len(matrix)-1
            colIsBorder = col == 0 or col == len(matrix[row])-1
            # check if either is a border
            isBorder = rowIsBorder or colIsBorder
            if matrix[row][col] == 1 and isBorder:
                # do dfs and mark 1s in aux ds
                findOnesConnectedToBorder1(
                    matrix, row, col, onesConnectedToBorder)

    # traverse inner matrix & mark all as 0 accept index in aux ds
    for row in range(1, len(matrix)-1):
        for col in range(1, len(matrix[row]-1)):
            if onesConnectedToBorder[row][col]:
                continue
            matrix[row][col] = 0
    return (matrix)


def findOnesConnectedToBorder1(matrix, i, j, oCTB):
    # skip when out of index or element is not 1 or value at index in aux ds is True
    if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] != 1 or oCTB[i][j] == True:
        return

    oCTB[i][j] = True
    findOnesConnectedToBorder1(matrix, i+1, j, oCTB)  # down
    findOnesConnectedToBorder1(matrix, i-1, j, oCTB)  # up
    findOnesConnectedToBorder1(matrix, i, j+1, oCTB)  # right
    findOnesConnectedToBorder1(matrix, i, j-1, oCTB)  # left


# final solution prevents use of aux data and instead change border connected 1s to 2 in the input matrix.
# Next traverse whole matrix again and change 2s to 1 and 1s to 0
# O(w*h) time | O(w*h) space (stack for dfs) better avg space than prev soln


def removeIslands(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            # check if we are on border indexes
            if row == 0 or col == 0 or row == len(matrix)-1 or col == len(matrix[0])-1:
                findOnesConnectedToBorder2(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] = 1 if matrix[row][col] == 2 else 0

    return matrix


def findOnesConnectedToBorder2(m, i, j):
    if i < 0 or j < 0 or i >= len(m) or j >= len(m[0]) or m[i][j] != 1:
        return

    m[i][j] = 2
    findOnesConnectedToBorder2(m, i+1, j)
    findOnesConnectedToBorder2(m, i-1, j)
    findOnesConnectedToBorder2(m, i, j+1)
    findOnesConnectedToBorder2(m, i, j-1)


print(removeIslands([
    [1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 0, 1],
]))
