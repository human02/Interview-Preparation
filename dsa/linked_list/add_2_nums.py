"""

2. Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.

"""


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Solution:
    def addNums(self, l1, l2):
        head1 = l1
        head2 = l2

        carry = 0
        # for new list
        dummyHead = ListNode(-1)
        curr = dummyHead
        while head1 or head2 or carry:  # if either of these are true
            val1 = head1.value if head1 else 0
            val2 = head2.value if head2 else 0

            curr_sum = val1 + val2 + carry

            carry = curr_sum // 10
            newNode = ListNode(curr_sum % 10)

            curr.next = newNode
            curr = curr.next  # move to the next node
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        return dummyHead.next
