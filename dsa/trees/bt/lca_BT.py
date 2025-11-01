"""
LCA in BT

Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).

Examples:
Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 1
Output : 3

Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 4
Output : 5

Input : root = [7, 1, 2, 8, 10, 4, 5, null, 6], p = 6, q = 10
Output: 1

Constraints:
2 <= Number of Nodes <= 105
-106 <= node.val <= 106
All values in tree are unique.
"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


"""
The LCA can be identified as one of the following: it may be located within the left subtree, 
the right subtree, or it might be the root node itself if the two nodes are distributed across both subtrees. 
The fundamental idea is that the LCA is the deepest node that serves as an ancestor to both target nodes, 
representing the point where their paths to the root diverge.
"""


class Solution:
    def find_LCA(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        elif right is None:
            return left
        else:
            return root
