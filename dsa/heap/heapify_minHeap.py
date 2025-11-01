"""
Heapify Algorithm

Given an array nums representing a min-heap and two integers ind and val, set the value at index ind (0-based)
to val and perform the heapify algorithm such that the resulting array follows the min-heap property.
Modify the original array in-place, no need to return anything.

Examples:
Input: nums = [1, 4, 5, 5, 7, 6], ind = 5, val = 2
Output: [1, 4, 2, 5, 7, 5]
Explanation: After setting index 5 to 2, the resulting heap in array form = [1, 4, 5, 5, 7, 2]
Parent of nums[5] = nums[2] = 5 > nums[5] = 2, so they are swapped.
Final array = [1, 4, 2, 5, 7, 5]

Input: nums = [2, 4, 3, 6, 5, 7, 8, 7], ind = 0, val = 7
Output: [3, 4, 7, 6, 5, 7, 8, 7]
Explanation: After setting index 0 to 7, the resulting heap in array form =[7, 4, 3, 6, 5, 7, 8, 7]
The parent of nums[2] = nums[0] = 7 > nums[2] = 3, so they are swapped. No further swaps are needed.
Final array = [3, 4, 7, 6, 5, 7, 8, 7]

Constraints:
-> 1 <= nums.length <= 105
-> -104 <= nums[i] <= 104
-> 0 <= ind < nums.length
-> -104 <= val <= 104
-> nums represents a min-heap
"""

"""
Idea: For MinHeap implementation
- When the new value is < updated value (it should be up), so heapifyUp.
    - Calculate Parent Index
    - Check if parent idx > -1 and  parent element < updated value
        - update the value and make recursive call
    
- When the new value is > updated value (it should be down), so heapifyDown.
    - Keep track of smallestIdx
        - Calculate left and right child indexes
        - Check if left child indexes is within range and the value is smaller than smallest index
        - Check if right child indexes is within range and the value is smaller than smallest index
        - Check if smallestIdx is changed from original - then swap element and make recursive call
"""


# TC - O(log(n)), SC - O(log(n))
class Solution:
    def heapifyDown(self, arr, ind):
        n = len(arr)
        smallest_idx = ind
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

    def heapifyUp(self, arr, ind):

        parentIdx = (ind - 1) // 2
        if parentIdx > -1 and arr[parentIdx] > arr[ind]:
            arr[ind], arr[parentIdx] = arr[parentIdx], arr[ind]
            self.heapifyUp(arr, parentIdx)
        return

    def heapify(self, nums, ind, val):
        # if curr value is replaced by smaller value:
        if nums[ind] > val:
            nums[ind] = val
            self.heapifyUp(nums, ind)
        # if curr value is replaced by larger value:
        else:
            nums[ind] = val
            self.heapifyDown(nums, ind)
        return


if __name__ == "__main__":
    nums = [1, 4, 5, 5, 7, 6]
    ind = 5
    val = 2

    # Input array
    print("Input array:", end=" ")
    for it in nums:
        print(it, end=" ")

    # Creating an object of the Solution class
    sol = Solution()

    # Function call to heapify the array
    sol.heapify(nums, ind, val)

    # Output array
    print("\nModified array after heapifying:", end=" ")
    for it in nums:
        print(it, end=" ")
    print("\n")

    nums = [2, 4, 3, 6, 5, 7, 8, 7]
    ind = 0
    val = 7
    # Input array
    print("Input array:", end=" ")
    for it in nums:
        print(it, end=" ")

    # Function call to heapify the array
    sol.heapify(nums, ind, val)

    # Output array
    print("\nModified array after heapifying:", end=" ")
    for it in nums:
        print(it, end=" ")
    print("\n")
