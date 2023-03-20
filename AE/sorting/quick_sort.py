"""

  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Quick Sort algorithm to sort the array.

  Sample Input:
    array = [8, 5, 2, 9, 5, 6, 3]
  
  Sample Output:
    [2, 3, 5, 5, 6, 8, 9]
    
"""

# Best: O(nlog(n)) time | O(log(n)) space
# Average: O(nlog(n)) time | O(log(n)) space
# Worst: O(n^2) time | O(log(n)) space when division give smaller array of 1 element
def quickSort(array):
    quickSortHelper(0, len(array) - 1, array)
    return array


def quickSortHelper(startIdx, endIdx, array):
    # When array has 1 element
    if startIdx >= endIdx:
        return

    # Assign pointer the values
    leftPtr = startIdx + 1
    rightPtr = endIdx
    pivotPtr = startIdx

    # Running till the right ptr doesn't goes left to the left ptr
    while rightPtr >= leftPtr:
        # swap when elements at pivot > leftptr & elements at pivot < right ptr
        if array[leftPtr] > array[pivotPtr] and array[rightPtr] < array[pivotPtr]:
            swap(leftPtr, rightPtr, array)
        # inc left ptr as its already in place wrt to the pivot's final position
        if array[leftPtr] <= array[pivotPtr]:
            leftPtr += 1
        # dec right ptr as its already in place wrt to the pivot's final position
        if array[rightPtr] >= array[pivotPtr]:
            rightPtr -= 1
    # swapping crossed over right ptr with the pivot and now pivot is in its final place
    swap(rightPtr, pivotPtr, array)

    # Checking smaller subarray to reduce the runtime complexity, smaller will result in better complexity
    leftSubarrayIsSmall = ((rightPtr - 1) - startIdx) < (endIdx - (rightPtr + 1))
    if leftSubarrayIsSmall:
        quickSortHelper(startIdx, rightPtr - 1, array)
        quickSortHelper(rightPtr + 1, endIdx, array)
    else:
        quickSortHelper(rightPtr + 1, endIdx, array)
        quickSortHelper(startIdx, rightPtr - 1, array)


def swap(a, b, array):
    array[a], array[b] = array[b], array[a]
