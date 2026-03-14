"""

Maximum Width of BT

Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is
the maximum width among all levels. The width of a level is determined by measuring the distance between its end nodes,
which are the leftmost and rightmost non-null nodes. The length calculation additionally takes into account the null
nodes that would be present between the end nodes if a complete binary tree were to stretch down to that level.


Example 1
Input : root = [1, 3, 2, 5, 3, null, 9]
Output : 4
Explanation :
So if the below tree would be a complete binary tree then there would be total 4 nodes in the last level.
So the maximum width of the binary tree is between the nodes with value 5 and 9 is equal to 4.

Example 2
Input : root = [1, 3, 2, 5, null, null, 9, 6, null, 7]
Output : 7
Explanation :
If the below tree would be a complete binary tree then at last levels there would b 7 nodes including the node with value 6 and 7.
So the maximum width of binary tree is 7.

Example 3
Input : root = [5, 1, 2, 8, null, 4, 5, null, 6]
Output:

Constraints
    1 <= Number of Nodes <= 3000
    -1000 <= Node.val <= 1000

"""
