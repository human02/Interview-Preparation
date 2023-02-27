"""

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all quadruplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these quadruplets in no particular order.

  If no four numbers sum up to the target sum, the function should return an
  empty array.

  Sample Input:
    array = [7,6,4,-1,1,2]
    targetSum = 16

  Sample Output:
    [[7, 6, 4, -1], [7, 6, 1, 2]] 

"""

# Avg - O(n^2) time | O(n^2) space
# Worst - O(n^3) time | O(n^2) space


def fourNumberSum(array, targetSum):
    # dict to store sum ('q')
    allPairSums = {}
    resultQuadruplets = []

    # Skipping as 1st and final iteration doesn't do anything as discussed in conceptual overview
    # 1st iteration  - no value in the hash table is present.
    # Last iteration - there are no values after it to sum with it.
    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            currSum = array[i] + array[j]
            compliment = targetSum - currSum
            if compliment in allPairSums:
                # adding 'p'
                for pair in allPairSums[compliment]:
                    resultQuadruplets.append(pair + [array[i], array[j]])
        # find 'q' by iterating over each element before ith idx and creating pair.
        for k in range(0, i):
            currSum = array[i] + array[k]
            if currSum not in allPairSums:
                allPairSums[currSum] = [[array[i], array[k]]]
            else:
                allPairSums[currSum].append([array[i], array[k]])
    return resultQuadruplets
