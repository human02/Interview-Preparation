"""

  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.

  A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
  branch is a path of nodes in a tree that starts at the root node and ends at
  any leaf node.
"""

# DFS and sum at each leaf node and append to the result list.


# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

# O(n) time | O(n) space - helper function


def calculateBranchSums(node, runningSum, sums):
    # add in the end - case where node has either of the two children.
    if node is None:
        return

    # Sum to get the number
    newRunningSum = runningSum + node.value
    # next check for leaf node condition
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return

    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
