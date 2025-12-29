"""

Minimum time taken to burn the BT from a given Node

Given a target node data and a root of binary tree. If the target is set on fire,
determine the shortest amount of time needed to burn the entire binary tree.

It is known that in 1 second all nodes connected to a given node get burned.
That is its left child, right child, and parent.


Example 1
Input : root = [1, 2, 3, 4, null, 5, 6, null, 7]. target = 1
Output : 3
Explanation :
    The node with value 1 is set on fire.
    In 1st second it burns node 2 and node 3.
    In 2nd second it burns nodes 4, 5, 6.
    In 3rd second it burns node 7.

Example 2
Input : root = [1, 2, 3, null, 5, null, 4], target = 4
Output : 4
Explanation :
    The node with value 4 is set on fire.
    In 1st second it burns node 3.
    In 2nd second it burns node 1.
    In 3rd second it burns node 2.
    In 4th second it burns node 5.

Input : root = [1, 2, 3, 6, 5, 8, 4], target = 4
Output:

Constraints
    1 <= Number of Nodes <= 104
    -105 <= Node.val <= 105
    All Node.val values are unique.

"""
