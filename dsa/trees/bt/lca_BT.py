"""
LCA in BT

Given a root of binary tree, find the lowest common ancestor (LCA) of two given nodes (p, q) in the tree.
The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p
and q as descendants (where we allow a node to be a descendant of itself).

Examples:
Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 1
Output : 3

Input : root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4] , p = 5, q = 4
Output : 5

Input : root = [7, 1, 2, 8, 10, 4, 5, null, 6], p = 6, q = 10
Output: 1

Constraints:
2 <= Number of Nodes <= 105
-106 <= node.val <= 106
All values in tree are unique.
"""
