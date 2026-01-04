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
