"""
Difficulty - Easy

Two Number Sum


  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.


  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.


  You can assume that there will be at most one pair of numbers summing up to
  the target sum.


Input:
    array =  = [3, 5, -4, 8, 11, 1, -1, 6]
    targetSum = 10

Output:
    [-1, 11]

"""

# O(n^2) time | O(1) space


def twoNumberSum_brute(array, targetSum):
    length = len(array)
    for i in range(len(array)-1):
        first_num = array[i]
        for j in range(i+1, len(array)):
            second_num = array[j]
            if (first_num+second_num == targetSum):
                return [first_num, second_num]
    return []


# O(n) time | O(n) space
def twoNumberSum_hash(array, targetSum):
    res = []
    hash_dict = {}
    for i in range(len(array)):
        compliment = targetSum - array[i]
        if compliment not in hash_dict:
            hash_dict[array[i]] = True
        else:
            return [compliment, array[i]]


# O(nlog(n)) time beacuse of the sorting | O(1) space
def twoSum(array, targetSum):
    start = 0
    end = len(array)-1
    array.sort()
    while (start < end):
        currentSum = array[start] + array[end]
        if (currentSum == targetSum):
            return [array[start], array[end]]
        elif (currentSum < targetSum):
            start += 1
        else:
            end -= 1
    return []


print(twoNumberSum_hash([3, 5, -4, 8, 11, 1, -1, 6], 10))

-4, -1, 1, 3, 5, 6, 8, 11
