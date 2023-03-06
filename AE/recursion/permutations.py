"""

"""


def getPermutations(array):
    permutations = []
    helper(array, [], permutations)
    return permutations


# Upper bound - O(n^2*n!) time | O(n*n!) space
# Roughly - O(n*n!) time | O(n*n!) space
def helper(arr, currPerm, permutations):
    # check if we have ay numbers left in the array
    # never want to append empty array to the permutation, its where you can assign something else for the empty array
    if not len(arr) and len(currPerm):
        permutations.append(currPerm)
    else:
        for i in range(len(arr)):
            # generate array w/o the element
            newArray = arr[:i] + arr[i + 1 :]
            newPerm = currPerm + [arr[i]]
            helper(newArray, newPerm, permutations)
