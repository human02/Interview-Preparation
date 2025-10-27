"""
Aggressive Cows

Given an array nums of size n, which denotes the positions of stalls, and an integer k, which denotes the number of
aggressive cows, assign stalls to k cows such that the minimum distance between any two cows is the maximum possible.
Find the maximum possible minimum distance.

Examples:
Input: n = 6, k = 4, nums = [0, 3, 4, 7, 10, 9]
Output: 3
Explanation: The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed
at positions [0, 3, 7, 10]. Here the distances between cows are 3, 4, and 3 respectively.
We cannot make the minimum distance greater than 3 in any ways.

Input : n = 5, k = 2, nums = [4, 2, 1, 3, 6]
Output: 5
Explanation: The maximum possible minimum distance between any two cows will be 5 when 2 cows are placed at positions [1, 6].

Input : n = 5, k = 3, nums = [10, 1, 2, 7, 5]
Output: 4

Constraints:
  2 <= n <= 105
  2 <= k <= n
  0 <= nums[i] <= 109

"""


class Solution:
    def isPossible(self, gap, nums, k):
        c = 1
        n = len(nums)
        last = nums[0]
        for i in range(1, n):
            if nums[i] - last >= gap:
                c += 1
                last = nums[i]
        return c >= k

    def find_distance_brute(self, nums, k):
        n = len(nums)
        nums.sort()
        limit = nums[-1] - nums[0]
        ans = 0
        for i in range(1, limit + 1):
            if self.isPossible(i, nums, k):
                ans = i
        return ans

    def find_distance_optimal(self, nums, k):
        n = len(nums)
        low = 1
        nums.sort()
        high = nums[-1] - nums[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if self.isPossible(mid, nums, k):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_distance_brute([0, 3, 4, 7, 10, 9], 4))
    print(obj.find_distance_optimal([0, 3, 4, 7, 10, 9], 4))
    print(obj.find_distance_brute([4, 2, 1, 3, 6], 2))
    print(obj.find_distance_optimal([4, 2, 1, 3, 6], 2))
    print(obj.find_distance_brute([10, 1, 2, 7, 5], 3))
    print(obj.find_distance_optimal([10, 1, 2, 7, 5], 3))
