"""
LCA in BST

Given the root node of a binary search tree (BST) and two node values p,q.
Return the lowest common ancestors(LCA) of the two nodes in BST.

Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , p = 2, q = 4
Output : [3]

Input : root = [5, 3, 6, 2, 4, null, 7] , p = 2, q = 7
Output : [5]

Input : root = [2, 1, 4, null, null, 3, 6] , p = 1, q = 6
Output : [2]

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def find_LCA(self, root, p, q):
        if root is None:
            return root
        if root.data < p and root.data < q:
            return self.find_LCA(root.right, p, q)
        elif root.data > p and root.data > q:
            return self.find_LCA(root.left, p, q)
        else:
            return root


if __name__ == "__main__":
    # Create a sample binary tree
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    sol = Solution()

    # Find the LCA of nodes with values 5 and 1
    ans = sol.find_LCA(root, 5, 1)
    if ans:
        print("LCA(5, 1) =", ans.data)
    else:
        print("LCA(5, 1) is not present in the tree")

    # Find the LCA of nodes with values 5 and 4
    ans = sol.find_LCA(root, 5, 4)
    if ans:
        print("LCA(5, 4) =", ans.data)
    else:
        print("LCA(5, 4) is not present in the tree")
