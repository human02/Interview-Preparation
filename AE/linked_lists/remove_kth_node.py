"""
"""
# This is an input class. Do not edit.

# O(n) time | O(1) space


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    count = 1
    first = head
    second = head
    while count <= k:
        second = second.next
        count += 1

# case when already you reached out the list when moving the second coounter
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

# at the end of this loop, first will be just a node before kth node
    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
