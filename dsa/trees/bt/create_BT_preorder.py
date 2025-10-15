"""
Construct Binary Tree from Preorder and Inorder Traversal
Solved
You are given two integer arrays preorder and inorder.

preorder is the preorder traversal of a binary tree
inorder is the inorder traversal of the same tree
Both arrays are of the same size and consist of unique values.
Rebuild the binary tree from the preorder and inorder traversals and return its root.

Example 1:
Input: preorder = [1,2,3,4], inorder = [2,1,3,4]
Output: [1,2,3,null,null,null,4]


Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder, inorder):
        # inorder = left, root, right
        # preorder = root left right
        inorder_mp = {val: idx for idx, val in enumerate(inorder)}

        def helper(prestart, preend, instart, inend):
            if prestart > preend or instart > inend:
                return None
            root_val = preorder[prestart]
            root = TreeNode(root_val)
            inroot = inorder_mp[root_val]
            numleft = inroot - instart
            root.left = helper(prestart + 1, prestart + numleft, instart, inroot - 1)
            root.right = helper(prestart + numleft + 1, preend, inroot + 1, inend)
            return root

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
