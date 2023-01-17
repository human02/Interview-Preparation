"""

"""


class BST:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None

# use bfs for iterative solution

# O(n) time | O(n) space - leaves at a time can be n/2 which make space as O(n)


def invertBST_iter(node):
    queue = [node]
    while len(queue) > 0:
        # removes element from front
        currNode = queue.pop(0)
        # If node is NULL then skip the node
        if currNode is None:
            continue
        # do swap stuff here
        swapLeftRight(currNode)
        # add left and right of the node to the queue
        queue.append(currNode.left)
        queue.append(currNode.right)


def swapLeftRight(tree):
    tree.left, tree.right = tree.right, tree.left

# no queue for recursive
# O(n) time | O(d) space - active stack at max will be = depth of tree


def invertBinaryTree_recursive(tree):
    # base case
    if tree is None:
        return
    #  swap here
    swapLeftRight(tree)
    invertBinaryTree_recursive(tree.left)
    invertBinaryTree_recursive(tree.right)
