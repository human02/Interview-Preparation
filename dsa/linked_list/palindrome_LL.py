""" """


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head):
        # If no element or 1 element, then its Palindrome
        if not head or not head.next:
            return True

        slow, fast = head, head
        # Idea is to find middle, reverse second and compare each

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Seggregate and reverse 2nd part
        second = slow.next
        second = self.reverseLL(second)

        # Traverse and compare each
        left, right = head, second
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

    def reverseLL(self, head):
        curr, prev = head, None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
