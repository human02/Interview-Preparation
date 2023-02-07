"""
Heap is a binary tree a special types that has 2 additional properties:
- Completeness: it needs to have all its levels filled completely, except the last level if its partly filled up needs to be filled from left to right.
- Heap property: 
    for min heap = every node's value needs to be <= the values of its children nodes.
    for max heap = every node's value needs to be >= the values of its children nodes.

Heap is in no way sorted. They can be represented neatly in the array:

currentNode = i
childOne = 2i + 1
childTwo = 2i + 2
parentNode = floor((i-1)/2)
"""
# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) time | O(1) space
    def buildHeap(self, array):
        # find first parent and keep
        firstParentIdx = ((len(array) - 1) - 1) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            print(currentIdx)
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        # traverse childOneIdx until endIdx and then compare with childTwoIdx value and swap and update childOneIdx
        childOneIdx = 2 * currentIdx + 1
        while childOneIdx <= endIdx:
            # Check if the 2nd child is out of heap
            childTwoIdx = 2 * currentIdx + 2 if 2 * currentIdx + 2 <= endIdx else -1
            # If childTwo within heap
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = 2 * currentIdx + 1
            # means we are done with sifting
            else:
                return

    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        # find parent and swap if curr value < parent value (min heap, opp for max heap)
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]

    # O(log(n)) time | O(1) space
    def remove(self):
        # Swap the element with the 1st element in heap and then apply siftdown.
        self.swap(0, len(self.heap) - 1, self.heap)
        eleToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return eleToRemove

    # O(log(n)) time | O(1) space
    def insert(self, value):
        # Insert value at the ned and then call sift up
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    # O(1) time | O(1) space
    def swap(self, idxOne, idxTwo, heap):
        heap[idxOne], heap[idxTwo] = heap[idxTwo], heap[idxOne]
