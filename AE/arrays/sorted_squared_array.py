"""

  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.

  Input:
  [1,2,3,5,6,8,9]

  Output:
  [1,4,9,25,36,64,81]

"""
# Major catch is the -ve numbers in this question

# O(nlogn) time | O(n) space


def sortedSquaredArray(array):
    # Write your code here.
    result = [0]*len(array)
    # Two pointers for checking the larger value and one for result array indexing
    start, end, i = 0, len(array)-1, len(array)-1

    # Starting from end as it shows no number can be bigger than it.
    while (start <= end):
        if (abs(array[start]) < abs(array[end])):
            result[i] = array[end]**2
            end -= 1
        else:
            result[i] = array[start]**2
            start += 1
        i -= 1
    return (result)
