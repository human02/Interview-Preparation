"""

"""

# The idea is to keep the root value b/w a range (a min value and a max value),
# Initiate the range from -inf to +inf
# If we traverse the left subtree - update the max value of the range to current node value and check if value in range
# If we traverse the right subtree - update the min value of the range to current node value and check if value in range
# If we reach a None value then we can say that this is a valid BST and we recursively climb up.


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return helper(tree, float("-inf"), float("inf"))


# O(n) time | O(d) space where d is depth of the tree due to call stack
def helper(tree, minVal, maxVal):
    # case where we reach the end of the tree and found that the tree is valid
    if tree is None:
        return True

    # check if value is not following the req condition
    if tree.value < minVal or tree.value >= maxVal:
        return False

    # If not then traverse recursively:
    leftIsValid = helper(tree.left, minVal, tree.value)
    rightIsValid = helper(tree.right, tree.value, maxVal)

    # in the end return True if both trees are valid else False
    return leftIsValid and rightIsValid
