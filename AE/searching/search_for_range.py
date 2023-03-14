"""
  Write a function that takes in a sorted array of integers as well as a target
  integer. The function should use a variation of the Binary Search algorithm to
  find a range of indices in between which the target number is contained in the
  array and should return this range in the form of an array.

  The first number in the output array should represent the first index at which
  the target number is located, while the second number should represent the
  last index at which the target number is located. The function should return [-1, -1]
  if the integer isn't contained in the array.

Sample Input:
    array = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
    target = 45

Sample Output:
    [4, 9]

"""


# O(log(n)) time | O(n) space due to recursive stack
def searchForRange(array, target):
    # Checking if target not found
    finalRange = [-1, -1]
    # for checking left extreme case
    alteredBS(array, target, 0, len(array) - 1, finalRange, True)
    alteredBS(array, target, 0, len(array) - 1, finalRange, False)
    return finalRange


def alteredBS(array, target, left, right, finalRange, goLeft):
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < target:
            left = mid + 1
        elif array[mid] > target:
            right = mid - 1
        # case where we found the target element
        else:
            # checking if its either extreme elems of target value
            # check left case:
            if goLeft:
                # its the last target value on the left
                if mid == 0 or array[mid - 1] != target:
                    finalRange[0] = mid
                    return
                # more target values to the left therefore iterate left
                else:
                    right = mid - 1
            # check right case:
            else:
                # its the last target value on the right
                if mid == len(array) - 1 or array[mid + 1] != target:
                    finalRange[1] = mid
                    return
                # more target values to the right therefore iterate right
                else:
                    left = mid + 1
