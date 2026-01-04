"""

Construct a BST from a preorder traversal

Given an array of integers preorder, which represents the preorder traversal of a BST
(i.e., binary search tree), construct the tree and return its root. It is guaranteed
that it is always possible to find a binary search tree with the given requirements for
the given test cases.

Note : As there can be many possible correct answers, the compiler outputs true if the solution
is correct, else false.


Example 1
Input : preorder = [8, 5, 1, 7, 10, 12]
Output : [8, 5, 10, 1, 7, null, 12]

Example 2
Input : preorder = [1, 3]
Output : [1, null, 3]

Example 3
Input : preorder = [5, 3, 2, 4, 6, 7]

Output:
[5, 3, 6, 4, 2, null, 7]
[5, 6, 3, 2, 4, null, 7]
[5, 3, 6, 2, 4, null, 7]
[5, 6, 3, 4, 2, null, 7]

Constraints
    1 <= preorder.length <= 100
    1 <= preorder[i] <= 1000
    All the values of preorder are unique.

"""


class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    # TC - O(n^2)in worst case - skew tree, SC - O(1)
    def createBST_brute(self, preorder):
        """
        Idea:
        - first node is root
        - any node < root, is in left subtree
        - any node > root, is in right subtree
        """
        if not preorder:
            return preorder

        def helper(nodes):
            if not nodes:
                return None

            root_val = nodes[0]
            root_node = TreeNode(root_val)

            # Find the first element greater than root_val
            # Start from index 1 to avoid infinite recursion
            split_idx = 1
            while split_idx < len(nodes) and nodes[split_idx] < root_val:
                split_idx += 1

            root_node.left = helper(nodes[1:split_idx])
            root_node.right = helper(nodes[split_idx:])
            return root_node

        return helper(preorder)


# Function to print the tree in-order for testing
def inorderTraversal(self, root):
    if root:
        self.inorderTraversal(root.left)
        print(root.data, end=" ")
        self.inorderTraversal(root.right)


if __name__ == "__main__":
    obj = Solution()
    print(obj.createBST_brute([8, 5, 1, 7, 10, 12]))
    print(obj.createBST_brute([1, 3]))
    print(obj.createBST_brute([5, 3, 2, 4, 6, 7]))
