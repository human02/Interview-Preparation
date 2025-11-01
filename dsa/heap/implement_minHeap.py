"""
Implement Min Heap

You need to implement the Min Heap with the following given methods:

insert (x) -> insert value x to the min heap
getMin -> Output the minimum value from min heap
exctractMin -> Remove the minimum element from the heap
heapSize -> return the current size of the heap
isEmpty -> returns if heap is empty or not
changeKey (ind, val) -> update the value at given index to val (index will be given 0-based indexing)
initializeHeap -> Initialize the heap

Examples:
Input : operation = [ "initializeheap", "insert", "insert", "insert", "getMin", "heapSize", "isEmpty",
 "extractMin", "changeKey" , "getMin" ]
nums = [ [4], [1], [10], [0, 16] ]
Output : [ null, null, null, null, 1, 3, 0, null, null, 10 ]
Explanation : In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd, 4th operation we insert 4, 1, 10 to the heap respectively. The heap after 4th operation will be -> [1, 4, 10].
In 5th operation we output the minimum element from the heap i.e. 1.
In 6th operation we output the size of the current heap i.e. 3.
In 7th operation we output whether the heap is empty or not i.e. false (0).
In 8th operation we remove the minimum element from heap. So the ne heap becomes -> [4, 10].
In 9th operation we change the 0th index element to 16. So new heap becomes -> [16, 10]. After heapify -> [10, 16].
In 10th operation we output the minimum element of the heap i.e. 10.

Input : operation = [ "initializeheap", "insert", "insert", "extractMin", "getMin", "insert",
"heapSize", "isEmpty", "extractMin", "changeKey" , "getMin" ]
nums = [ [4], [1], [1], [0, 2] ]
Output : [ null, null, null, null, 4, null, 2, 0, null, null, 2 ]
Explanation : In 1st operation we initialize the heap to empty heap.
In 2nd, 3rd operation we insert 4, 1 to the heap respectively. The heap after 4th operation will be -> [1, 4].
In 4th operation we remove the minimum element from heap. So the ne heap becomes -> [4].
In 5th operation we output the minimum element of the heap i.e. 4.
In 6th operation we operation we insert 1 to the heap. The heap after 6th operation will be -> [1, 4].
In 7th operation we output the size of the current heap i.e. 2.
In 8th operation we output whether the heap is empty or not i.e. false (0).
In 9th operation we remove the minimum element from heap. So the ne heap becomes -> [4].
In 10th operation we change the 0th index element to 2. So new heap becomes -> [2].
In 11th operation we output the minimum element of the heap i.e. 2.

Constraints:
1 <= n <= 105
-105 <= nums[i] <= 105
"""


# SC - O(n)
class MinHeap:

    # TC - O(1)
    def __init__(self):
        self.arr = []
        self.count = 0

    # TC - O(log(n))
    def heapifyUp(self, arr, ind):
        parent_idx = (ind - 1) // 2
        if parent_idx > -1 and arr[parent_idx] > arr[ind]:
            arr[ind], arr[parent_idx] = arr[parent_idx], arr[ind]
            self.heapifyUp(arr, parent_idx)
        return

    # TC - O(log(n))
    def heapifyDown(self, arr, ind):
        smallest_idx = ind
        n = len(arr)
        leftChild_idx = 2 * ind + 1
        rightChild_idx = 2 * ind + 2
        if leftChild_idx < n and arr[leftChild_idx] < arr[smallest_idx]:
            smallest_idx = leftChild_idx
        if rightChild_idx < n and arr[rightChild_idx] < arr[smallest_idx]:
            smallest_idx = rightChild_idx
        if smallest_idx != ind:
            arr[smallest_idx], arr[ind] = arr[ind], arr[smallest_idx]
            self.heapifyDown(arr, smallest_idx)
        return

    # TC - O(log(n))
    def insert(self, x):
        self.arr.append(x)
        self.heapifyUp(self.arr, self.count)
        self.count += 1
        return

    # TC - O(1)
    def getMin(self):
        if self.isEmpty():
            return None
        return self.arr[0]

    # TC - O(log(n))
    def extractMin(self):
        ele = self.arr[0]
        # Swap the top value with the value at last index
        self.arr[0], self.arr[self.count - 1] = self.arr[self.count - 1], self.arr[0]
        self.arr.pop()
        self.count -= 1
        # Heapify the root value downwards
        if self.count > 0:
            self.heapifyDown(self.arr, 0)
        return ele

    # TC - O(1)
    def heapSize(self):
        return self.count

    # TC - O(1)
    def isEmpty(self):
        return len(self.arr) == 0

    # TC - O(log(n))
    def changeKey(self, ind, val):
        if self.arr[ind] > val:
            self.arr[ind] = val
            self.heapifyUp(self.arr, ind)
        else:
            self.arr[ind] = val
            self.heapifyDown(self.arr, ind)
        return

    # TC - O(1)
    def initializeHeap(self):
        self.arr.clear()
        self.count = 0
