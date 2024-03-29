"""

"""

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    prev = None
    while (head.next != None):
        temp = head.next
        head.next = prev
        prev = head
        head = temp

    # last element not linked with previous
    head.next = prev
    prev = head
    return prev
