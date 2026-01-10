"""

Maximum path sum

In a binary tree, a path is a list of nodes where there is an edge between every pair of neighbouring nodes.
A node may only make a single appearance in the sequence.

The total of each node's values along a path is its path sum.
Return the largest path sum of all non-empty paths given the root of a binary tree.

Note: The path does not have to go via the root.

Example 1
Input : root = [20, 9, -10, null, null, 15, 7]
Output : 34
Explanation : The path from node 15 to node 9 has maximum path sum.
The path is 15 -> -10 -> 20 -> 9.

Example 2
Input : root = [-10, 9, 20, null, null, 15, 7]
Output : 42
Explanation : The path from node 15 to node 7 has maximum path sum.
The path is 15 -> 20 -> 7.

Example 3
Input : root = [1, 2, 3, null, 4]
Output:

Constraints
    1 <= Number of Nodes <= 3*104
    -103 <= Node.val <= 103

"""


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class Solution:
    """
    Idea:
    - Comprehensive exploration of every potential path is required.
    - At each node, we check the max sum
        - Sum @ each node = Node_val + (maxLft_ST+maxRgt_ST)
    - We find the max of these sums
    """

    def maxPathSum(self, root):

        self.maxi = float("-inf")

        def helper(node):
            if not node:
                return 0

            lh = max(0, helper(node.left))
            rh = max(0, helper(node.right))
            self.maxi = max(self.maxi, node.data + lh + rh)

            return node.data + max(lh, rh)

        helper(root)
        return self.maxi


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(6)
    root.left.right.right.right = TreeNode(7)

    obj = Solution()
    print(obj.maxPathSum(root))
