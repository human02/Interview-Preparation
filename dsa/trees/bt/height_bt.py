"""
Find Height of a BT
"""


class Binary_TreeNode:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def find_height(self, root):
        if root is None:
            return 0
        lh = self.find_height(root.left)
        rh = self.find_height(root.right)

        return 1 + max(lh, rh)


if __name__ == "__main__":
    obj = Solution()
    obj.find_height()
