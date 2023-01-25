"""

  Write a function that takes in the head of a Singly Linked List that contains
  a loop (in other words, the list's tail node points to some node in the list
  instead of None/null). The function should return the node (the actual node--not just its value)
  from which the loop originates in constant space.

  Each LinkedList node has an integer value as well as next value pointing to the next node in the list.

  Input:
    head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 
                               ^         |
                               |         v
                               9 <- 8 <- 7
  Output:
    4 -> 5 -> 6 
    ^         |
    |         v
    9 <- 8 <- 7
    

"""
# hare and tortoise algorithm:
# one counter +1, another counter +2 at each step and eventually if both meet.
# let t travel total of X distance, so h will travel 2X distance
# diagram and maths will reach to the point that after meeting, if we run both pointer at +1 pace
# with t starting from head dgain, both will reach the node where the loop starts.


class LinkedList():
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) - time | O(1) - space


def findLoop(head):
    tortoise = head.next
    hare = head.next.next
    while (tortoise != hare):
        tortoise = tortoise.next
        hare = hare.next.next

    # put hare or tortoise either back to head position
    tortoise = head
    # now move both at same pace
    while (hare != tortoise):
        hare = hare.next
        tortoise = tortoise.next
    # where they meet gives the start of the loop
    return hare
