"""
Delete a node in BST

Given the root node of a binary search tree (BST) and a value key.
Return the root node of the BST after the deletion of the node with the given key value.
Note: As there can be many correct answers, the compiler returns true if the answer is correct, otherwise false.

Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , key = 3
Output : [5, 4, 6, 2, null, null, 7]

Input : root = [5, 3, 6, 2, 4, null, 7] , key = 0
Output : [5, 3, 6, 2, 4, null, 7]
Explanation : The tree does not have node with value 0.

Input : root = [5, 3, 6, 2, 4, null, 7] , key = 5
Output: [4, 3, 6, 2, null, null, 7]

Constraints:
1 <= Number of nodes <= 104
-108 <= Node.val <= 108
All values in tree are unique.
-108 <= key <= 108

"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    def delete_node(self, root, key):
        if root is None:
            return None

        if root.data == key:
            return self.connector_helper(root)

        node = root
        while node:
            if node.data > key:
                if node.left and node.left.data == key:
                    node.left = self.connector_helper(node.left)
                    break
                else:
                    node = node.left
            else:
                if node.right and node.right.data == key:
                    node.right = self.connector_helper(node.right)
                    break
                else:
                    node = node.right
        return root

    def connector_helper(self, root):
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp = root.left
            leftMostNode_RST = root.right
            while leftMostNode_RST.left:
                leftMostNode_RST = leftMostNode_RST.left
            # Add the delete node's left to the left of the right's leftmost node
            leftMostNode_RST.left = temp
        return root.right


if __name__ == "__main__":
    # Create a sample binary search tree
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    sol = Solution()

    def inorder(node):
        if not node:
            return
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

    print("Inorder traversal of original tree:")
    inorder(root)
    # Delete node with key 3 from the tree
    root = sol.delete_node(root, 3)

    # Helper function to print tree in-order
    def inorder(node):
        if not node:
            return
        inorder(node.left)
        print(node.data, end=" ")
        inorder(node.right)

    print("\n\nInorder traversal of resulting tree:")
    inorder(root)
    print()
