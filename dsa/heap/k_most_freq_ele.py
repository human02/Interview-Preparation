"""

Top K Frequent Elements

Given an integer array nums and an integer k, return any order list of the k most frequent elements in nums.
Your solution must run in better than O(n log n) time, where n = nums.length.

Examples:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Explanation: 1 appears 3 times, 2 appears 2 times, 3 appears once.
       The two most-frequent elements are 1 and 2.

Input: nums = [4,4,6,6,7], k = 2
Output: [4,6]
Explanation: 4 and 6 both occur twice (highest), 7 occurs once.

Input: nums = [-1,-1,-2,-2,-2,-3], k = 1
Output: [-2]

Constraints:
    1 ≤ nums.length ≤ 105
    -104 ≤ nums[i] ≤ 104
    1 ≤ k ≤ number of distinct elements in nums
    The answer is guaranteed to be unique.

"""

from collections import Counter
import heapq


class Solution:
    # TC - O(nlogk) , SC - O(n)
    def findKMost(self, nums, k):
        """
        Idea:
            - Find out the frequency of each element using Counter
            - Use heap to store the -freq, key from Counter - MaxHeap
            - Pop out k-1 times from heap and store in a new list
            - Return this list
        """
        freq = Counter(nums)

        pq = []
        for key, val in freq.items():
            heapq.heappush(pq, (-1 * val, key))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(pq)[1])
        return result

    # TC - O(n) , SC - O(n)
    def findKMost_optimal(self, nums, k):
        """
        Idea:
            - Find out the frequency of each element using Counter
            - Use heap to store the -freq, key from Counter - MaxHeap
            - Pop out k-1 times from heap and store in a new list
            - Return this list
        """

        freq_map = Counter(nums)

        # BUCKET SORT - Create buckets (index = frequency)
        buckets = [[] for _ in range(len(nums) + 1)]

        # Populate bucket with freq and num
        for num, freq in freq_map.items():
            buckets[freq].append(num)

        # Collect top k from highest frequency
        result = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result

        return result


if __name__ == "__main__":
    obj = Solution()
    print(f"{obj.findKMost([1, 1, 1, 2, 2, 3], 2)}")
    print(f"{obj.findKMost([4,4,6,6,7], 2)}")
    print(f"{obj.findKMost([-1,-1,-2,-2,-2,-3], 1)}")
    print()
    print(f"{obj.findKMost_optimal([1, 1, 1, 2, 2, 3], 2)}")
    print(f"{obj.findKMost_optimal([4,4,6,6,7], 2)}")
    print(f"{obj.findKMost_optimal([-1,-1,-2,-2,-2,-3], 1)}")
