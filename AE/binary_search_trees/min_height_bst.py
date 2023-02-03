"""
"""

# O(nlog(n)) time | O(n) space
def minHeightBst(array):
    return constructMinHeightBST(array, None, 0, len(array) - 1)


def constructMinHeightBST(array, bst, startIdx, endIdx):
    # Case when end crosses start index
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    newBst = BST(array[midIdx])
    # Case where there is no BST/no root node
    if bst is None:
        bst = newBst
    else:
        bst.insert(array[midIdx])
    constructMinHeightBST(array, bst, startIdx, midIdx - 1)
    constructMinHeightBST(array, bst, midIdx + 1, endIdx)
    return bst


# O(n) time | O(n) space
# not using the naive insert function given and hence saving time complexity
def minHeightBst(array):
    return constructMinHeightBST(array, None, 0, len(array) - 1)


def constructMinHeightBST(array, bst, startIdx, endIdx):
    # Case when end crosses start index
    if endIdx < startIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    newBST = BST(array[midIdx])
    # Case where there is no BST/no root node
    if bst is None:
        bst = newBST
    else:
        if array[midIdx] < bst.value:
            bst.left = newBST
            bst = bst.left
        else:
            bst.right = newBST
            bst = bst.right
    constructMinHeightBST(array, bst, startIdx, midIdx - 1)
    constructMinHeightBST(array, bst, midIdx + 1, endIdx)
    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
