"""

"""

# [7,10,12,7,9,14]
# maxSums [7,10,19,19(keeping max btw prev sum and currSum),28,31]
# So based on that we can derive the below formula:

#          |--> maxSum(i-1)
# maxSum[i] --|                         max of either the two.
#          |--> maxSum(i-2) + arr[i]


def maxSubsetSumNoAdjacent(array):
    # edge case - empty array
    if not len(array):
        return 0
    # edge case - array with one element
    elif len(array) == 1:
        return array[0]
    # copy array as we also want 1st 2 numbers
    maxSum = array[:]
    maxSum[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        maxSum[i] = max(maxSum[i-1], maxSum[i-2]+array[i])
    return maxSum[-1]
