"""
find the depth of each branch of a binary tree
"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# O(n) - time space


def maxHeight(root):
    heights = []
    helper(root, 0, heights)
    # return height - gives list of height from left branch to right
    return max(heights)


def helper(node, runningHeight, heights):
    if node is None:
        return
    newRunnningHeight = runningHeight + 1
    if (node.left is None and node.right is None):
        heights.append(newRunnningHeight)
    helper(node.left, newRunnningHeight, heights)
    helper(node.right, newRunnningHeight, heights)
