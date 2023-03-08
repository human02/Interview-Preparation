"""

  Write a function that takes in the head of a Singly Linked List and an integer 'k', 
  shifts the list in place (i.e., doesn't create a brand new list) by k positions, and returns its new head.


  Shifting a Linked List means moving its nodes forward or backward and wrapping
  them around the list where appropriate. For example, shifting a Linked List
  forward by one position would make its tail become the new head of the linked
  list.

  
  Whether nodes are moved forward or backward is determined by whether 'k' is positive or negative.
  
  You can assume that the input Linked List will always have at least one node;
  in other words, the head will never be None/null.
  
  Sample Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 
    k = 2

  Sample Output:
    4 -> 5 -> 1 -> 2 -> 3 

  
"""

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def shiftLinkedList(head, k):
    p1 = head
    lngth = 0

    # find length of the LL
    l1 = head
    while l1 is not None:
        l1 = l1.next
        lngth += 1

    # Check case when k is greater than length of the LL:
    k = k % lngth

    # check case when k is negative:
    if k < 0:
        k = lngth - abs(k) % lngth

    # check if k = 0:
    if k == 0:
        return head

    # When 'k' is 0 or <= length of LL: follow the common steps below.

    # offsetting the 1st ptr by k value
    for i in range(k):
        p1 = p1.next

    # reaching the position for both pointers
    p2 = head
    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next

    # updating all the pointers
    p1.next = head
    head = p2.next
    p2.next = None

    return head
