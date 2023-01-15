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
