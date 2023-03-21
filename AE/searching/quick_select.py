"""

  Write a function that takes in an array of distinct integers as well as an
  integer 'k' and that returns the kth smallest integer in that array.
  The function should do this in linear time, on average.

  Sample Input:
    array = [8, 5, 2, 9, 7, 6, 3]
    k = 3

  Sample Output:
    5
"""
# O(n) time - best, avg | O(1) space as its non-recursive
def quickselect(array, k):
    position = k - 1
    return quickselectHelper(array, 0, len(array) - 1, position)


def quickselectHelper(array, startIdx, endIdx, position):
    while True:
        # check interviewer to handle this case however they want you to handle it.
        if startIdx > endIdx:
            raise Exception(
                "Your algorithm shouldn't never comes here, it missed th element"
            )

        pivotPtr = startIdx
        leftPtr = startIdx + 1
        rightPtr = endIdx

        while leftPtr <= rightPtr:
            if array[leftPtr] > array[pivotPtr] and array[rightPtr] < array[pivotPtr]:
                swap(leftPtr, rightPtr, array)
            if array[leftPtr] <= array[pivotPtr]:
                leftPtr += 1
            if array[rightPtr] >= array[pivotPtr]:
                rightPtr -= 1
        swap(rightPtr, pivotPtr, array)

        # checking the position of the pivot element:
        if position == rightPtr:
            return array[rightPtr]
        # eliminate the right sub-array
        elif position < rightPtr:
            endIdx = rightPtr - 1
        # eliminate the left sub-array
        else:
            startIdx = rightPtr + 1


def swap(a, b, array):
    array[a], array[b] = array[b], array[a]
