"""

  You're given the head of a Singly Linked List whose nodes are in sorted order
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The
  Linked List should be modified in place (i.e., you shouldn't create a brand
  new list), and the modified Linked List should still have its nodes sorted
  with respect to their values.

  Each LinkedList node has an integer value as well as a next node pointing to the 
  next node in the list or to None/null if it's the tail of the list
  

  Input:
    Linked List =  1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6 

  Output:
    Linked List = 1 -> 3 -> 4 -> 5 -> 6
    
"""

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList
    while (currNode):
        nextDistinctNode = currNode.next
        # iterating till elemnt is either null or not equal to currNode value
        while (nextDistinctNode and nextDistinctNode.value == currNode.value):
            nextDistinctNode = nextDistinctNode.next

        # attach current node pointer to the above found unique node
        currNode.next = nextDistinctNode
        # finally iterate to next node
        currNode = nextDistinctNode

    return linkedList
