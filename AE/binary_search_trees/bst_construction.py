"""
The iterative solution is better due to lesser space complexity
"""


class BST:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

    # avg case -> time O(log(n)), space - O(1)
    # worst case -> time O(n), space - O(1)

    def insert(self, value):
        currNode = self
        while True:
            if value < currNode.value:
                # reached leaf node on left tree
                if currNode.left is None:
                    currNode.left = BST(value)
                    break
                else:
                    currNode = currNode.left
            else:
                # reached leaf node on right tree
                if currNode.right is None:
                    currNode.right = BST(value)
                    break
                else:
                    currNode = currNode.right
        return self

    # avg case -> time O(log(n)), space - O(1)
    # worst case -> time O(n), space - O(1)

    def contains(self, value):
        currNode = self
        while currNode is not None:
            if value < currNode.value:
                currNode = currNode.left
            elif value > currNode.value:
                currNode = currNode.right
            else:
                return True
        return False

    # avg case -> time O(log(n)), space - O(1)
    # worst case -> time O(n), space - O(1)

    def remove(self, value, parentNode=None):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # case where the node is not a leaf node (2 children node are there case)
                if currentNode.left is not None and currentNode.right is not None:
                    # we need smallest value of the right subtree
                    currentNode.value = currentNode.right.getMinValue()
                    # now remove that node
                    currentNode.right.remove(currentNode.value, currentNode)
                # root node case (no Parent node)
                elif parentNode is None:
                    if currentNode.left is not None:
                        currentNode.value = currentNode.left.value
                        currentNode.right = currentNode.left.right
                        currentNode.left = currentNode.left.left
                    elif currentNode.right is not None:
                        currentNode.value = currentNode.right.value
                        currentNode.left = currentNode.right.left
                        currentNode.right = (
                            currentNode.right.right
                        )  # the statement order matters
                    else:
                        pass  # case with only one node tree
                #
                elif parentNode.left == currentNode:
                    parentNode.left = (
                        currentNode.left
                        if currentNode.left is not None
                        else currentNode.right
                    )
                elif parentNode.right == currentNode:
                    parentNode.right = (
                        currentNode.left
                        if currentNode.left is not None
                        else currentNode.right
                    )
                break
        return self

    def getMinValue(
        self,
    ):
        currentNode = self
        while currentNode.left is not None:
            currentNode = currentNode.left
        return currentNode.value
