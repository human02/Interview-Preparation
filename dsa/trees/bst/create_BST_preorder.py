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

    # TC - O(nlogn) + O(n), SC - O(n)
    def createBST_better(self, preorder):
        """
        Idea:
        - Inorder traversal of BST gives sorted list of all BST nodes
        - Sort the list of nodes given as input, it will be BST inorder
        - Create Tree same using pre and inorder like in BT
        """
        inorder = reversed(preorder, reverse=False)
        inMap = {val: idx for idx, val in enumerate(inorder)}

        def helper(preStr, preEnd, inStr, inEnd):
            if preStr > preEnd or inStr > inEnd:
                return None
            rootVal = preorder[preStr]
            rootNode = TreeNode(rootVal)
            inRoot = inMap[rootVal]
            nums_left = inRoot - inStr
            rootNode.left = helper(preStr + 1, preStr + nums_left, inStr, inRoot - 1)
            rootNode.right = helper(preStr + nums_left + 1, preEnd, inRoot + 1, inEnd)
            return rootNode

        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)

    # TC - O(n), SC - O(h) due to recursive stack
    def createBST_optimal(self, preorder):
        """
        Idea:
        - Eliminate need for sorting
        - a tree BT or BST concept, using only Upper bound concept
        - At each node, left/right nodes can only have values < upper bound
        - When no case fufilled, we go to right or back up based on upper bound checks:
            - Left -> node.val is upperbound
            - Right -> root.val is upperbound / transfer the upperbound
        - Check until preorder runs out or when we cant place any element in the tree.
        """

        def helper(pre, bound, index):
            # If all elements are used or the next element
            # is greater than the bound, return None
            if index[0] == len(pre) or pre[index[0]] > bound:
                return None

            root = TreeNode(pre[index[0]])
            index[0] += 1

            root.left = helper(pre, root.data, index)
            root.right = helper(pre, bound, index)

            # Return the constructed subtree's root
            return root

        """
        Integers are immutable, meaning a function receives a local copy of the reference; 
        incrementing it only reassigns that local name to a new object, leaving the parent's 
        value unchanged.

        By wrapping the value in a mutable object like a list (e.g., index = [0]), you pass a 
        reference to the same container. When any recursive call modifies index[0], it alters 
        the contents of that shared container in memory, allowing all calls to track a single, 
        synchronized state 
        """
        return helper(preorder, float("inf"), [0])


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
