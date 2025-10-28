"""
Bottom view of BT

Given root of binary tree, return the bottom view of the binary tree.
The bottom view of a binary tree is the set of nodes visible when the tree is viewed from the bottom.
Return nodes from the leftmost node to the rightmost node. Also if 2 nodes are outside the shadow of the tree
and are at the same position then consider the node that appears later in level traversal.

Examples:
Input : root = [20, 8, 22, 5, 3, null, 25, null, null, 10 ,14]
Output : [5, 10, 3, 14, 25]
Explanation : From left to right the path is as follows :
First we encounter node with value 5.
Then we have nodes 8 , 10 but from bottom only 10 will be visible.
Next we have 20 , 3 but from bottom only 3 will be visible.
Next we have 14 , 22 but from bottom only 14 will be visible.
Then we encounter node with value 25.


Input : root = [20, 8, 22, 5, 3, 4, 25, null, null, 10 ,14]
Output : [5, 10, 4, 14, 25]
Explanation : From left to right the path is as follows :
First we encounter node with value 5.
Then we have nodes 8 , 10 but from bottom only 10 will be visible.
Next we have 20 , 3 and 4. The 3 and 4 will be nodes visible from bottom but as the node 4 appears later from left to right ,
so only node 4 will be considered visible. Next we have 14 , 22 but from bottom only 14 will be visible.
Then we encounter node with value 25.



Input: root = [10, 20, 30, 40, 60]
Output: [40, 20, 60, 30]

Constraints:
1 <= Number of Nodes <= 104
-103 <= Node.val <= 103
"""
