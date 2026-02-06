"""

215. Kth Largest Element in an Array

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:
    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

"""

import heapq


class Solution:
    # TC -  O(nlogn), SC - O(1)
    def findKthLargest_brute(self, nums, k):
        n = len(nums)
        nums.sort()
        return nums[n - k]

    # TC -  O(nlogn), SC - O(n)
    def findKthLargest_better(self, nums, k):
        pq = []

        for num in nums:
            heapq.heappush(pq, -1 * num)

        for _ in range(k - 1):
            heapq.heappop(pq)

        return pq[0] * -1

    # TC - O(n log k), SC - O(log k)
    def findKthLargest_heap_OP(self, nums, k):
        pq = []

        # Push first k elements
        for i in range(k):
            heapq.heappush(pq, nums[i])

        # For remaining elements, if larger than min, replace min
        for i in range(k, len(nums)):
            if nums[i] > pq[0]:
                heapq.heappop(pq)
                heapq.heappush(pq, nums[i])

        # The root of min-heap is the kth largest
        return pq[0]

    # TC - O(n + range), SC - O(range)
    def findKthLargest_optimal(self, nums, k):
        """
        Count Sort idea
        """
        minV = min(nums)
        maxV = max(nums)

        count_buckets = maxV - minV + 1
        freq = [0] * count_buckets

        for num in nums:
            freq[num - minV] += 1

        for i in range(count_buckets - 1, -1, -1):
            if k > freq[i]:
                k -= freq[i]
            else:
                return i + minV
        return -1
