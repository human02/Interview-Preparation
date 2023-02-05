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

    # 7th method to implement --> O(1) time | O(1) space
    def setHead(self, node):
        # if LL is empty
        if self.head is None:
            self.head = node
            self.tail = node
            return
        # else just insert node before current head
        self.insertBefore(self.head, node)

    # 8th method to implement --> O(1) time | O(1) space
    def setTail(self, node):
        # if LL is empty
        if self.tail is None:
            self.setHead(node)
            return
        # else just insert node after current tail
        self.insertAfter(self.tail, node)

    # 5th method to implement --> O(1) time | O(1) space where
    def insertBefore(self, node, nodeToInsert):
        # Check if we are inserting a node in a list with only one node, just return in such case
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        # remove the node if already in the LL:
        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # Now the other node bindings:
        # incase prev is none, meaning its head and we should update the head
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # 6th method to implement --> O(1) time | O(1) space
    def insertAfter(self, node, nodeToInsert):
        # Check if we are inserting a node in a list with only one node, just return in such case
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)
        nodeToInsert.next = node.next
        nodeToInsert.prev = node

        # Now the other bindings:
        # If next is None, then update the tail:
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # 9th method to implement --> O(p) time | O(1) space where p is the position and it can be > n
    def insertAtPosition(self, position, nodeToInsert):
        #
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        count = 1
        while node is not None and count != position:
            node = node.next
            count += 1

        # now either we got None or reached the position
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # 4th method to implement --> O(n) time | O(1) space
    def removeNodesWithValue(self, value):
        node = self.head
        # traverse the ll
        while node is not None:
            #  create to keep track as remove function will remove th node bindings
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # 2nd method to implement --> O(1) time | O(1) space
    def remove(self, node):
        # there can be 3 cases:
        # node we want to remove is head, just iterate the head to next node
        if node == self.head:
            self.head = self.head.next
        # node we want to remove is tail, just iterate back to the previous node
        if node == self.tail:
            self.tail = self.tail.prev
        # node we want to remove is in the middle, use helper and remmove the bidings
        self.removeNodeBindings(node)

    # 1st method to implement --> O(n) time | O(1) space
    def containsNodeWithValue(self, value):
        node = self.head
        # we traverse either until we either find value or None
        while node is not None and node.value is not value:
            node = node.next

        # necessary to check if we found none or a node with value
        return node is not None

    # 3rd method to implement --> O(1) time | O(1) space
    def removeNodeBindings(self, node):
        # if prev is not None, then change prev binding:
        if node.prev is not None:
            node.prev.next = node.next
        # if next is not None, then change next binding:
        if node.next is not None:
            node.next.prev = node.prev
        # Also remove nodes nother bindings:
        node.prev = None
        node.next = None
