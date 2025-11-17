"""

Sort LL

Given the head of a singly linked list. Sort the values of the linked list in non-decreasing order and
return the head of the modified linked list.


Examples:
Input: head -> 5 -> 6 -> 1 -> 2 -> 1
Output: head -> 1 -> 1 -> 2 -> 5 -> 6
Explanation: 1 <= 1 <= 2 <= 5 <= 6

Input: head -> 6 -> 5 -> -1 -> -2 -> -3
Output: head -> -3 -> -2 -> -1 -> 5 -> 6
Explanation: -3 <= -2 <= -1 <= 5 <= 6

Input: head -> -1 -> -2 -> -3 -> -1
Output: head -> -3 -> -2 -> -1 -> -1

Constraints:
    0 <= number of nodes in the linked list <= 1000
    -104 <= ListNode.val <= 104

"""
