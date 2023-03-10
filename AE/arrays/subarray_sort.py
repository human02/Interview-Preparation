"""

  Write a function that takes in an array of at least two integers and that
  returns an array of the starting and ending indices of the smallest subarray
  in the input array that needs to be sorted in place in order for the entire
  input array to be sorted (in ascending order).


  If the input array is already sorted, the function should return [-1, -1]

"""

# Idea is to:
"""
- check if the value is not in order
- find the min and max values of the vallues that are not in order
- get the ideal of these 2 values in the input array 
"""


# O(n) time | O(1) space
def subarraySort(array):
    # store the min and max values of the unsorted parts
    minOutofOrder = float("inf")
    maxOutofOrder = float("-inf")

    for i in range(len(array)):
        num = array[i]
        # if we find num to be OOO then we find min and max values of the unsorted values.
        if isOutofOrder(i, num, array):
            minOutofOrder = min(minOutofOrder, num)
            maxOutofOrder = max(maxOutofOrder, num)

    # Check the edge case where inp array is already sorted (ascending order),
    # Can also compare with maxOutofOrder
    if minOutofOrder == float("inf"):
        return [-1, -1]

    # check minOOO element position in inp array
    left = 0
    while array[left] <= minOutofOrder:
        left += 1

    # check maxOOO element position in inp array
    right = len(array) - 1
    while array[right] >= maxOutofOrder:
        right -= 1

    return [left, right]


def isOutofOrder(i, num, array):
    """
    -Ideally we want to check prev and next number for an idx 'i'
    -But in certain cases, start and end; we will have only 1 number
    """
    # Start case:
    if i == 0:
        # check only the next and not the prev index
        return array[i + 1] < num

    # End case:
    if i == len(array) - 1:
        # check the prev index only
        return array[i - 1] > num

    # Normal case where both prev and next are available
    return array[i - 1] > num or array[i + 1] < num


print(subarraySort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]))
