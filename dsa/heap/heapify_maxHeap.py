""" """


class Solution:
    def heapify(self, nums, ind, val):
        if nums[ind] > val:
            nums[ind] = val
            self.heapifyDown(nums, ind)
        else:
            nums[ind] = val
            self.heapifyUp(nums, ind)
        return

    def heapifyDown(self, arr, ind):
        n = len(arr)
        largest_idx = ind
        leftChild_idx = 2 * ind + 1
        rightChild_idx = 2 * ind + 2
        if leftChild_idx < n and arr[leftChild_idx] > arr[largest_idx]:
            largest_idx = leftChild_idx
        if rightChild_idx < n and arr[rightChild_idx] > arr[largest_idx]:
            largest_idx = rightChild_idx

        if largest_idx != ind:
            arr[ind], arr[largest_idx] = arr[largest_idx], arr[ind]
            self.heapifyDown(arr, largest_idx)
        return

    def heapifyUp(self, arr, ind):
        parent_idx = (ind - 1) // 2
        if parent_idx > -1 and arr[parent_idx] < arr[ind]:
            arr[ind], arr[parent_idx] = arr[parent_idx], arr[ind]
            self.heapifyUp(arr, parent_idx)
        return


if __name__ == "__main__":
    nums = [7, 5, 6, 4, 1, 2]  # Valid max-heap
    ind = 5
    val = 3

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
