"""

  Write a function that takes in a sorted array of distinct integers as well as a target
  integer. The caveat is that the integers in the array have been shifted by
  some amount; in other words, they've been moved to the left or to the right by
  one or more positions. For example, [1, 2, 3, 4] might have been turned into [3, 4, 1, 2]


  The function should use a variation of the Binary Search algorithm to
  determine if the target integer is contained in the array and should return
  its index if it is, otherwise -1.

  array =  = [45, 61, 71, 72, 73, 0, 1, 21, 33, 37]
  target = 33

"""

# O(log(n)) time | O(1) space
def shiftedBinarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        leftEle = array[left]
        rightEle = array[right]
        midEle = array[mid]
        if midEle == target:
            return mid

        # CHECKING WHERE ORDER IS CORRECT:
        # means the left to mid are in sorted order
        # [45,61,71,72,73,0,1,21,33,44] example for this case
        elif leftEle < midEle:
            # explore left part
            if target < midEle and target >= leftEle:
                right = mid - 1
            # explore left part
            else:
                left = mid + 1
        # means the right to end are in sorted order
        # [61,71,72,73,0,1,21,33,44,45] example for this case
        else:
            if target > midEle and target <= rightEle:
                left = mid + 1
            else:
                right = mid - 1
    return -1
