"""

"""

# O(log(n)) time (on avg) O(n) time (worst)  | O(n) space as its recursive


def findClosestValueInBstRecur(tree, target):
    return helperRecursive(tree, target, closest=float("inf"))


def helperRecursive(tree, target, closest):
    # when traversed till end (base condition)
    if tree is None:
        return closest
    # compare and update value
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    # now traverse based on the target value:
    if target < tree.value:
        return helperRecursive(tree.left, target, closest)
    elif target > tree.value:
        return helperRecursive(tree.right, target, closest)
    # when target is same as node value
    else:
        return closest


# O(log(n)) time (on avg) O(n) time (worst)  | O(1) space as its not using call stack


def findClosestValueInBstIter(tree, target):
    return helperIterative(tree, target, closest=float("inf"))


def helperIterative(tree, target, closest):
    currNode = tree
    while currNode is not None:
        # compare and update value
        if abs(target - closest) > abs(target - currNode.value):
            closest = currNode.value
        # now traverse based on the target value:
        if target < currNode.value:
            currNode = currNode.left
        elif target > currNode.value:
            currNode = currNode.right
        # when target is same as node value
        else:
            break
    return closest


# This is the class of the input tree. Do not edit.


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
