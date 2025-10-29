"""
Two sum in BST

Given the root of a binary search tree and an integer k.
Return true if there exist two elements in the BST such that their sum is equal to k otherwise false.

Examples:
Input : root = [5, 3, 6, 2, 4, null, 7] , k = 9
Output : true
Explanation : The BST contains multiple pair of nodes that sum up to k.
3 + 6 => 9.
5 + 4 => 9.
2 + 7 => 9.

Input : root = [5, 3, 6, 2, 4, null, 7] , k = 14
Output : false
Explanation : There is no pair in given BST that sum up to k.

Input : root = [5, 3, 6, 2, 4, null, 7] , k = 12
Output:true

Constraints:
1 <= Number of Nodes <= 104
-104 <= Node.val <= 104
-105 <= k <= 105
"""


class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class Solution:
    # TC - O(n), SC - O(n)
    def find_two_sum_brute(self, root, k):
        # Inorder of BST gives sorted elements
        sorted_ele = []

        def inorder(root):
            if root is None:
                return root
            inorder(root.left)
            sorted_ele.append(root.data)
            inorder(root.right)

        """
        # Without using outside List Variable - sorted_ele. This will return a list of elements
        def inorder(root):
            if root is None:
                return []
            return inorder(root.left) + [root.data] + inorder(root.right)
        """

        inorder(root)
        # Using two sum - 2 pointer approach to find answer
        left, right = 0, len(sorted_ele) - 1
        while left < right:
            curr_sum = sorted_ele[left] + sorted_ele[right]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                left += 1
            else:
                right -= 1
        return False


if __name__ == "__main__":
    # Example tree: [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    k = 9
    solution = Solution()
    result = solution.find_two_sum_brute(root, k)
    print(f"\n{result}\n")  # Output: True
