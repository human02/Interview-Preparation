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
