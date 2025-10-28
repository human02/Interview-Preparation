"""
Bottom view of BT

Given root of binary tree, return the bottom view of the binary tree.
The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree
and are at the same position then consider the node that appears later in level traversal.

Examples:
Input : root = [20, 8, 22, 5, 3, null, 25, null, null, 10 ,14]
Output : [5, 10, 3, 14, 25]
Explanation : From left to right the path is as follows :
First we encounter node with value 5.
Then we have nodes 8 , 10 but from bottom only 10 will be visible.
Next we have 20 , 3 but from bottom only 3 will be visible.
Next we have 14 , 22 but from bottom only 14 will be visible.
Then we encounter node with value 25.


Input : root = [20, 8, 22, 5, 3, 4, 25, null, null, 10 ,14]
Output : [5, 10, 4, 14, 25]
Explanation : From left to right the path is as follows :
First we encounter node with value 5.
Then we have nodes 8 , 10 but from bottom only 10 will be visible.
Next we have 20 , 3 and 4. The 3 and 4 will be nodes visible from bottom but as the node 4 appears later from left to right ,
so only node 4 will be considered visible. Next we have 14 , 22 but from bottom only 14 will be visible.
Then we encounter node with value 25.



Input: root = [10, 20, 30, 40, 60]
Output: [40, 20, 60, 30]

Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103
"""

from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    def bottom_view(self, root):
        ans = []
        mp = {}
        q = deque([(root, 0)])
        while q:
            node, vertical = q.popleft()
            mp[vertical] = node.data
            if node.left:
                q.append((node.left, vertical - 1))
            if node.right:
                q.append((node.right, vertical + 1))
        for _, val in sorted(mp.items()):
            ans.append(val)
        return ans


if __name__ == "__main__":
    # Creating a sample binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(10)
    root.left.left.right = TreeNode(5)
    root.left.left.right.right = TreeNode(6)
    root.right = TreeNode(3)
    root.right.right = TreeNode(10)
    root.right.left = TreeNode(9)

    solution = Solution()

    # Get the Bottom View traversal
    bottom_view = solution.bottom_view(root)

    # Print the result
    print("Bottom View Traversal: ")
    for node in bottom_view:
        print(node, end=" ")
