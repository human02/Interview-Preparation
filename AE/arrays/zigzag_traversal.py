"""

  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in zigzag order.

  Zigzag order starts at the top left corner of the two-dimensional array, goes
  down by one element, and proceeds in a zigzag pattern all the way to the
  bottom right corner.

  Sample Input:
     = [
        [1,  3,  4, 10],
        [2,  5,  9, 11],
        [6,  8, 12, 15],
        [7, 13, 14, 16],
        ]  
  
  Sample Output:
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

"""


# O(n) time | O(n) complexity
def zigzagTraverse(array):
    # rows
    height = len(array) - 1
    # columns
    width = len(array[0]) - 1
    result = []

    currRow = 0
    currCol = 0
    # direction tracking
    goingDown = True

    while not isOutOfBounds(currRow, currCol, height, width):
        # append current value
        result.append(array[currRow][currCol])

        # if goingDown
        if goingDown:
            # turning case - last row or first col
            if currRow == height or currCol == 0:
                goingDown = False
                # last row
                if currRow == height:
                    currCol += 1
                # last column
                else:
                    currRow += 1
            # if its normal
            else:
                currCol -= 1
                currRow += 1

        # if goingUp
        else:
            # turning case - last col or first row
            if currRow == 0 or currCol == width:
                goingDown = True
                if currCol == width:
                    currRow += 1
                else:
                    currCol += 1
            # normal
            else:
                currRow -= 1
                currCol += 1
    return result


def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width
