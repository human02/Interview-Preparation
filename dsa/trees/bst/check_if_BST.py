"""

Check if a tree is a BST or not

Given the root node of a binary tree. Return true if the given binary tree is a binary search tree(BST) else false.

A valid BST is defined as follows:
The left subtree of a node contains only nodes with key strictly less than the node's key.
The right subtree of a node contains only nodes with key strictly greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Examples:
Input : root = [5, 3, 6, 2, 4, null, 7]
Output : true

Input : root = [5, 3, 6, 4, 2, null, 7]
Output : false
Explanation : The node 4 and node 2 violates the BST rule of smaller to left and larger to right.

Input : root = [2, 1, 3]
Output: true

Constraints:
    1 <= Number of Nodes <= 104
    -231 <= Node.val <= 231 - 1

"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    # TC - O(n), SC - O(n)
    def isBST(self, root):
        return self.isValid(root, float("-inf"), float("inf"))

    def isValid(self, node, minV, maxV):
        if node is None:
            return True
        if node.data <= minV or node.data >= maxV:
            return False
        return self.isValid(node.left, minV, node.data) and self.isValid(
            node.right, node.data, maxV
        )


if __name__ == "__main__":
    obj = Solution()
    root = TreeNode(7)
    root.left = TreeNode(5)
    root.right = TreeNode(10)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(15)

    solution = Solution()
    print(solution.isBST(root))  # Output: False
