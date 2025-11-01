"""
Implement Max Heap

You need to implement the Max Heap with the following given methods:

insert (x) -> insert value x to the max heap
getMax -> Output the maximum value from max heap
extractMax -> Remove the maximum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
initializeHeap -> Initialize the heap
"""


# SC - O(n)
class MaxHeap:

    # TC - O(1)
    def __init__(self):
        self.arr = []
        self.count = 0

    # TC - O(log(n))
    def insert(self, x):
        self.arr.append(x)
        self.heapifyUp(self.arr, self.count)
        self.count += 1

    # TC - O(1)
    def getMax(self):
        if self.isEmpty():
            return None
        return self.arr[0]

    # TC - O(log(n))
    def heapifyDown(self, arr, ind):
        largest_idx = ind
        n = len(arr)
        leftChild_idx = 2 * ind + 1
        rightChild_idx = 2 * ind + 2
        if leftChild_idx < n and arr[leftChild_idx] > arr[largest_idx]:
            largest_idx = leftChild_idx
        if rightChild_idx < n and arr[rightChild_idx] > arr[largest_idx]:
            largest_idx = rightChild_idx
        if largest_idx != ind:
            arr[largest_idx], arr[ind] = arr[ind], arr[largest_idx]
            self.heapifyDown(arr, largest_idx)
        return

    # TC - O(log(n))
    def heapifyUp(self, arr, ind):
        parent_idx = (ind - 1) // 2
        if parent_idx > -1 and arr[parent_idx] < arr[ind]:
            arr[parent_idx], arr[ind] = arr[ind], arr[parent_idx]
            self.heapifyUp(arr, parent_idx)
        return

    # TC - O(log(n))
    def extractMax(self):
        ele = self.arr[0]
        self.arr[-1], self.arr[0] = self.arr[0], self.arr[-1]
        self.arr.pop()
        self.count -= 1
        if self.count > 0:
            self.heapifyDown(self.arr, 0)
        return ele

    # TC - O(1)
    def heapSize(self):
        return self.count

    # TC - O(1)
    def isEmpty(self):
        return self.count == 0

    # TC - O(log(n))
    def changeKey(self, ind, val):
        if self.arr[ind] > val:
            self.arr[ind] = val
            self.heapifyDown(self.arr, ind)
        else:
            self.arr[ind] = val
            self.heapifyUp(self.arr, ind)
        return

    # TC - O(1)
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0
