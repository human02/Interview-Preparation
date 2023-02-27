"""
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n+m) time where n and m are lengths of 2 LL | O(1) space
def mergeLinkedLists(headOne, headTwo):
    p1 = headOne
    p2 = headTwo
    # holds smaller value node
    p1Prev = None

    # Iterating through both lists
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            p1Prev = p1
            p1 = p1.next
        else:
            # additional step after 1st change is done
            if p1Prev is not None:
                p1Prev.next = p2
            # edge case when p1Prev is None
            # case when p1Prev doesn't have to change its next
            # order is important below
            p1Prev = p2
            p2 = p2.next
            p1Prev.next = p1

    # case when p2 list is larger than p1
    # rest values of p2 need to be added to p1Prev
    if p1 is None:
        p1Prev.next = p2

    # why not same check for p2?
    # When p1 is larger than p2, the list will be correct and no action is needed

    return headOne if headOne.value < headTwo.value else headTwo
