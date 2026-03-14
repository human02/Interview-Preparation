"""

Maximum Width of BT

Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is
the maximum width among all levels. The width of a level is determined by measuring the distance between its end nodes,
which are the leftmost and rightmost non-null nodes. The length calculation additionally takes into account the null
nodes that would be present between the end nodes if a complete binary tree were to stretch down to that level.


Example 1
Input : root = [1, 3, 2, 5, 3, null, 9]
Output : 4
Explanation :
So if the below tree would be a complete binary tree then there would be total 4 nodes in the last level.
So the maximum width of the binary tree is between the nodes with value 5 and 9 is equal to 4.

Example 2
Input : root = [1, 3, 2, 5, null, null, 9, 6, null, 7]
Output : 7
Explanation :
If the below tree would be a complete binary tree then at last levels there would b 7 nodes including the node with value 6 and 7.
So the maximum width of binary tree is 7.

Example 3
Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]
Output:

Constraints
    1 <= Number of Nodes <= 3000
    -1000 <= Node.val <= 1000

"""

from collections import deque


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class Solution:

    # TC - O(n), SC - O(n)
    def findMaxWidth(self, root):
        if not root:
            return 0

        q = deque([(root, 0)])
        maxWidth = float("-inf")
        while q:
            tnodes = len(q)
            currLevel = []
            _, leftPos = q[0]
            for i in range(tnodes):
                node, pos = q.popleft()
                currLevel.append(node)
                if node.left:
                    q.append((node.left, 2 * pos + 1))
                if node.right:
                    q.append((node.right, 2 * pos + 2))

                # Check to find rightmost at curr level
                if i == tnodes - 1:
                    rightPos = pos
            maxWidth = max(maxWidth, rightPos - leftPos + 1)

        return maxWidth


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    obj = Solution()
    print(obj.findMaxWidth(root))
