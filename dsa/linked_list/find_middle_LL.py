"""

Find Middle of Linked List

Given the head of a singly Linked List, return the middle node of the Linked List.
If the Linked List has an even number of nodes, return the second middle one.

Examples:
Input: head -> 3 -> 8 -> 7 -> 1 -> 3
Output(value at returned node): 7
Explanation: There are 5 nodes, so the middle node is the 3rd Node, with value 7.

Input: head -> 2 -> 9 -> 1 -> 4 -> 0 -> 4
Output(value at returned node): 4
Explanation: There are 6 nodes, thus both the 3rd and 4th nodes are middle. So the 2nd middle node (4th Node) is returned with value 4.

Input: head -> 3 -> 8 -> 1 -> 7 -> 0
Output: 1

Constraints:
1 <= number of Nodes in the Linked List <= 105
-104 <= ListNode.val <= 104

"""


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class Solution:
    def find_middle(self, head):
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
