"""

"""

# This is an input class. Do not edit.


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n,m)+1) time | O(max(n,m)+1) space, where n is length of ll1 and m of ll2

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    dummy = LinkedList(0)
    currNode = dummy
    carry = 0
    node1 = linkedListOne
    node2 = linkedListTwo

    while (node1 or node2 or carry != 0):
        # check if list 1 has a value or it is None
        value1 = node1.value if node1 else 0

        # check if list 2 has a value or it is None
        value2 = node2.value if node2 else 0

        sum = (value1 + value2 + carry) % 10
        carry = (value1 + value2 + carry) // 10

        #  creating new mode with the sum
        newNode = LinkedList(sum)

        # add to the new node and move forward
        currNode.next = newNode
        currNode = newNode

        node1 = node1.next if node1 else None
        node2 = node2.next if node2 else None

    return dummy.next
