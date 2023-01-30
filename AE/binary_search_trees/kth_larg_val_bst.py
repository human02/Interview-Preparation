"""

"""


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# Brute force method
# Idea: Inorder traversal gives sorted list of values.

# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    sortedValues = []
    helperTraverse(tree, sortedValues)
    return sortedValues[-k]


# Inorder traversal
def helperTraverse(tree, sortedValues):
    if tree is None:
        return
    helperTraverse(tree.left, sortedValues)
    sortedValues.append(tree.value)
    helperTraverse(tree.right, sortedValues)


# optimized solution
# doesn't make sense to traverse through from the smallest node(inorder)
# Efficient to do reverse Inorder traversal


# O(h+k) time as we need to go at most h height and then retun to prev and return | O(h) space atleast h stack in memory
def findKthLargestValueInBst(tree, k):
    treeInfo = TreeInfo(0, None)
    helperReverseTraverse(tree, k, treeInfo)
    # Once the reverse inorder traversal is done, then:
    return treeInfo.latestVisitedNodeValue


# This class is to keep track of the value of nodes visited & last value.
# The traversal will keep changing its values.
class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


def helperReverseTraverse(node, k, treeInfo):
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return
    helperReverseTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        # We dont want to traverse left if we already have visited k values on the right, thus we add it here
        helperReverseTraverse(node.left, k, treeInfo)
