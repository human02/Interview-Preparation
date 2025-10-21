"""
Detect a loop in LL

Given the head of a singly linked list. Return true if a loop exists in the linked list or return false.
A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index(0-based) of the node from where the loop starts.
Note that pos is not passed as a parameter.

Examples:
Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1
Output: true
Explanation: The tail of the linked list connects to the node at 1st index.

Input: head -> 1 -> 3 -> 7 -> 4, pos = -1
Output: false
Explanation: No loop is present in the linked list.

Input: head -> 6 -> 3 -> 7, pos = 0
Output:

Constraints:
0 <= number of nodes in the cycle <= 105
0 <= ListNode.val <= 104
pos is -1 or a valid index in the linked list
"""
