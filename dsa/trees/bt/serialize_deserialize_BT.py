"""
Serialize and Deserialize Binary Tree

Implement an algorithm to serialize and deserialize a binary tree.
Serialization is the process of converting an in-memory structure into a sequence of bits
so that it can be stored or sent across a network to be reconstructed later in another computer environment.
You just need to ensure that a binary tree can be serialized to a string and this string
can be deserialized to the original tree structure. There is no additional restriction on how
your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree.
You do not necessarily need to follow this format.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []

Constraints:
0 <= The number of nodes in the tree <= 1000.
-1000 <= Node.val <= 1000

"""

from collections import deque


class Binary_TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right


class Solution:
    # level Order traversal will serialize the tree
    def serialize(self, root):
        """
        Encodes the tree into a single string.
        :type root: Binary_TreeNode
        :rtype: str
        """
        if not root:
            return ""

        # Initialize an empty string to store the serialized data
        result = []
        # Use a queue for level-order traversal
        q = deque([root])

        # Perform level-order traversal
        while q:
            node = q.popleft()
            if node is None:
                result.append("#")
            else:
                result.append(str(node.data))
                q.append(node.left)
                q.append(node.right)

        # Return the serialized string
        return ",".join(result)

    def deserialize(self, data):
        """
        Decodes the encoded data to a tree.
        :type data: str
        :rtype: Binary_TreeNode
        """
        if not data:
            return None

        # Use a deque to tokenize the serialized data
        data = deque(data.split(","))
        # Read the root value from the serialized data
        root = Binary_TreeNode(int(data.popleft()))

        # Use a queue for level-order traversal
        q = deque([root])

        # Perform level-order traversal to reconstruct the tree
        while q:
            node = q.popleft()

            # Read the value of the left child from the serialized data
            left_val = data.popleft()
            if left_val != "#":
                left_node = Binary_TreeNode(int(left_val))
                node.left = left_node
                q.append(left_node)

            # Read the value of the right child from the serialized data
            right_val = data.popleft()
            if right_val != "#":
                right_node = Binary_TreeNode(int(right_val))
                node.right = right_node
                q.append(right_node)

        # Return the reconstructed root of the tree
        return root
