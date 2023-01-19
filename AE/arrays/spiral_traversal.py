"""
"""
# O(n) space time where n is the total num of elements in the array


def spiralTraverse_iter(array):
    result = []
    startRow, endRow = 0, len(array) - 1
    startCol, endCol = 0, len(array[0]) - 1

    while startCol <= endCol and startRow <= endRow:
        # moove right
        for col in range(startCol, endCol + 1):
            result.append(array[startRow][col])

        # move down
        for row in range(startRow + 1, endRow + 1):
            result.append(array[row][endCol])

        # move left
        for col in reversed(range(startCol, endCol)):
            #
            if startRow == endRow:
                break
            result.append(array[endRow][col])

        # move up
        for row in reversed(range(startRow + 1, endRow)):
            #
            if startCol == endCol:
                break
            result.append(array[row][startCol])

        # reduce
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1

    return result


# O(n) space time where n is the total num of elements in the array
def spiralTraverse_recursion(array):
    result = []
    spiralHelper(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
    return result


def spiralHelper(array, startRow, endRow, startCol, endCol, result):
    if (startRow > endRow or startCol > endCol):
        return
    # move right
    for col in range(startCol, endCol + 1):
        result.append(array[startRow][col])

    # move down
    for row in range(startRow + 1, endRow + 1):
        result.append(array[row][endCol])

    # move left
    for col in reversed(range(startCol, endCol)):
        #
        if startRow == endRow:
            break
        result.append(array[endRow][col])

    # move up
    for row in reversed(range(startRow + 1, endRow)):
        #
        if startCol == endCol:
            break
        result.append(array[row][startCol])

    spiralHelper(array, startRow+1, endRow-1, startCol+1, endCol-1, result)
    return result
