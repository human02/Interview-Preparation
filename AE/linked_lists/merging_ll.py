"""

"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n+m) time | O(n) space, n = length of 1st ll, m of 2nd


def mergingLinkedLists_Set(linkedListOne, linkedListTwo):
    llOneNodes = set()
    currOne = linkedListOne
    # add node values to set
    while (currOne):
        llOneNodes.add(currOne)
        currOne = currOne.next

    # traverse and if any element found, thats the merging point
    currTwo = linkedListTwo
    while (currTwo):
        if currTwo in llOneNodes:
            return currTwo
        currTwo = currTwo.next
    return None


# O(n+m) time | O(1) space, n = length of 1st ll, m of 2nd

def mergingLinkedLists_Length(linkedListOne, linkedListTwo):
    currOne = linkedListOne
    lenOne = 0
    while currOne:
        lenOne += 1
        currOne = currOne.next

    currTwo = linkedListTwo
    lenTwo = 0
    while currTwo:
        lenTwo += 1
        currTwo = currTwo.next

    # Find the length diff
    diff = abs(lenTwo - lenOne)

    # Find the bigger list and point to it
    biggerCurrentNode = linkedListOne if lenOne > lenTwo else linkedListTwo
    smallerCurrentNode = linkedListTwo if lenOne > lenTwo else linkedListOne
    #  Increase the bigger list by diff value
    for _ in range(diff):
        biggerCurrentNode = biggerCurrentNode.next

    # traverse both lists simultaneously until same node or None.
    # return eith of the node
    while (smallerCurrentNode is not biggerCurrentNode):
        smallerCurrentNode = smallerCurrentNode.next
        biggerCurrentNode = biggerCurrentNode.next
    return biggerCurrentNode
