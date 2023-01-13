"""
  Write a function that takes in an array of integers and returns a sorted
  version of that array. Use the Bubble Sort algorithm to sort the array.

  Input:
    array = [8,5,2,9,5,6,3]

  Output:
    array = [2,3,5,5,6,8,9]

"""

# O(n^2) - time | O(1) - space


def bubbleSort(array):
    isSorted = False
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
    return array

# As on each iteration, last number is on its correct place hence no need go till there

# O(n^2) - time | O(1) - space


def bubbleSortOptimised(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter += 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
