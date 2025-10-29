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
