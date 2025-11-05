"""
Check if two trees are identical or not

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Examples:
Input : p = [1, 2, 3] , q = [1, 2, 3]
Output : true
Explanation : Both trees images are shown below

Input : p = [1, 2, 1] , q = [1, 1, 2]
Output : false
Explanation : Both trees images are shown below

Input : p = [5, 1, 2, 8, null, null, 5, null, 4, null, null, 7 ], q = [5, 1, 2, 8, null, null, 4, null, 5, null, null, 7 ]
Output: false

Constraints:
0 <= Number of Nodes <= 100
-104 <= Node.val <= 104
"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def isIdentical(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.data != q.data:
            return False
        return self.isIdentical(p.left, q.left) and self.isIdentical(p.right, q.right)
