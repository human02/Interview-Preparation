"""
Difficulty - Easy

Binary Search

Write a function that takes in a sorted arrays of integers (array) and a target integer.
It returns -1 if target integer is not found in the input array else it returns the index of the target interger in the input array.

Input:
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33

Output:
    3

"""


def binarySearch(array, target):
    return bs_helper_recursion(array, target, 0, len(array)-1)


def bs_helper(array, target, start, end):
    while (start <= end):
        mid = (start+end)//2
        if (array[mid] == target):
            return mid
        elif (array[mid] > target):
            end = mid - 1
        else:
            start = mid + 1
    return -1


def bs_helper_recursion(array, target, start, end):
    if start > end:
        return -1
    mid = (start+end)//2
    if (target == array[mid]):
        return mid
    elif (target < array[mid]):
        return bs_helper_recursion(array, target, start, mid-1)
    else:
        return bs_helper_recursion(array, target, mid+1, end)


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 3))
