""" """


class Solution:
    def mergeSort(self, nums):
        self.mergeSortHelper(0, len(nums) - 1, nums)
        return nums

    def mergeSortHelper(self, low, high, arr):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSortHelper(low, mid, arr)
        self.mergeSortHelper(mid + 1, high, arr)
        self.merge(low, mid, high, arr)

    def merge(self, low, mid, high, arr):
        tmp = []
        left = low
        right = mid + 1
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                tmp.append(arr[left])
                left += 1
            else:
                tmp.append(arr[right])
                right += 1

        while left <= mid:
            tmp.append(arr[left])
            left += 1
        while right <= high:
            tmp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = tmp[i - low]
