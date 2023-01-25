"""

  Write a function that takes in a non-empty array of integers and returns the
  maximum sum that can be obtained by summing up all of the integers in a
  non-empty subarray of the input array. A subarray must only contain adjacent
  numbers (numbers next to each other in the input array).

    Input:  
        array = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]

    Output:
        19 // [1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1]

"""
# O(n) time | O(1) space
def kadanesAlgorithm(array):
    # Create 2 counter to keep track of max ending at an indx and max so far.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for i in array[1:]:
        maxEndingHere = max(i + maxEndingHere, i)
        maxSoFar = max(maxSoFar, maxEndingHere)
        print(f"here -> {maxEndingHere}\n sofar -> {maxSoFar}")
    return maxSoFar


print(kadanesAlgorithm([3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]))
