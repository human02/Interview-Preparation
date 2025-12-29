"""

Minimum time taken to burn the BT from a given Node

Given a target node data and a root of binary tree. If the target is set on fire,
determine the shortest amount of time needed to burn the entire binary tree.

It is known that in 1 second all nodes connected to a given node get burned.
That is its left child, right child, and parent.


Example 1
Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]. target = 1
Output : 3
Explanation :
    The node with value 1 is set on fire.
    In 1st second it burns node 2 and node 3.
    In 2nd second it burns nodes 4, 5, 6.
    In 3rd second it burns node 7.

Example 2
Input : root = [1, 2, 3, null, 5, null, 4], target = 4
Output : 4
Explanation :
    The node with value 4 is set on fire.
    In 1st second it burns node 3.
    In 2nd second it burns node 1.
    In 3rd second it burns node 2.
    In 4th second it burns node 5.

Input : root = [1, 2, 3, 6, 5, 8, 4], target = 4
Output:

Constraints
    1 <= Number of Nodes <= 104
    -105 <= Node.val <= 105
    All Node.val values are unique.

"""

from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right


class Solution:
    def timeToBurn(self, root, start):
        # create parent mapping
        q = deque([root])
        parent_mpp = {}
        while q:
            node = q.popleft()
            # only given the start value not the node with that value, hence finding it.
            if node.value == start:
                startNode = node
            if node.left:
                parent_mpp[node.left] = node
                q.append(node.left)
            if node.right:
                parent_mpp[node.right] = node
                q.append(node.right)

        # Radially expand
        visited = {startNode}
        q = deque([startNode])
        dist = 0
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
                if node in parent_mpp and parent_mpp[node] not in visited:
                    visited.add(parent_mpp[node])
                    q.append(parent_mpp[node])
            dist += 1

        # additional add in the last iteration
        return dist - 1


if __name__ == "__main__":
    obj = Solution()

    # Create the binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    start = 4

    print(obj.timeToBurn(root, start))
