"""

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.

  Input:
  [12, 3, 1, 2, -6, 5, -8, 6]
  targetSum = 0

  Output:
  [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

"""
# O(n^3) time | O(n) space

# not working


def threeNumberSum_brute(array, targetSum):
    # Write your code here.
    res = []
    count = 0
    temp = []
    for i in range(len(array)-2):
        j = i
        for j in range(j, len(array)-1):
            k = j
            for k in range(k, len(array)):
                if (array[i]+array[j]+array[k] == targetSum):
                    temp.append([array[i], array[j], array[k]])
                    sorted(temp)
                    res.append(temp)
                    temp = []
    return sorted(res)


# O(n^2) time | O(n) space


def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        left = i+1
        right = len(array) - 1
        while left < right:
            currentSum = array[i]+array[left]+array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum < targetSum:
                left += 1
            elif currentSum > targetSum:
                right -= 1
    return triplets
