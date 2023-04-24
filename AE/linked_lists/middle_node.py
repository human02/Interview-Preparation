"""

    You're given a Linked List with at least one node. Write a function
    that returns the middle node of the Linked List. If there are two middle
    nodes (i.e. an even length list), your function should return the second
    of these nodes.
  
    Each LinkedList node has an integer value as well as a next node pointing 
    to the next node in the list or to None/null if it's the tail of the list.

    Sample Input:
        linkedlist = 2 -> 7 -> 3 -> 5
    
    Sample Output:
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNodeBrute(linkedList):
    indx = linkedList
    l = 0
    while indx is not None:
        l += 1
        indx = indx.next

    if l % 2 == 0:
        l = l / 2
    else:
        l = l // 2

    idx = linkedList
    while l > 0:
        l -= 1
        idx = idx.next
    return idx


def middleNodeSlowFastPtr(linkedList):
    slow = linkedList
    fast = linkedList
    # 2nd condition to ensure
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow
