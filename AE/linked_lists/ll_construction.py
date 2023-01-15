"""

Write a DoublyLinkedList class that has a head and a tail, both o which points to
either a linked list Node or None/null. The class should support:
    -  Setting the head and tail of the linked list.
    -  Inserting nodes before and after other nodes as well as at given positions
       (the position of the head node is 1)
    -  Removing given nodes and removing nodes with given values.
    -  Searching for nodes with given values.

Note that the seHead, setTail, insertBefore, insertAfter, insertAtPosition, and remove methods
all take in actual Nodess as input parameters—not integers (except for insertAtPosition, which also
takes in an integer representing the position); this means that you don't need to create any new Nodes
in these methods. The input nodes can be either stand-alone nodes or nodes that are already in the linked
list. If they're nodes that are already in the linked list, the methods will effectively be moving the nodes
within the linked list. You won't be told if the input nodes are already in the linked list, so your code 
will have to defensively handle this scenario.

If you're doing this problem in an untyped language like Python or JavaScript,
you may want to look at the various function signatures in a typed language
like Java or TypeScript to get a better idea of what each input parameter is.
  
"""
# This is an input class. Do not edit.


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        # Write your code here.
        pass

    def setTail(self, node):
        # Write your code here.
        pass

    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        pass

    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        pass

    def removeNodesWithValue(self, value):
        # Write your code here.
        pass

    def remove(self, node):
        # Write your code here.
        pass

    def containsNodeWithValue(self, value):
        # Write your code here.
        pass
