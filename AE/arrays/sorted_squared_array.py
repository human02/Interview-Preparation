"""


"""


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
