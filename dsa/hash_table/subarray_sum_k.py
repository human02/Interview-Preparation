"""

560. Subarray Sum Equals K

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 104
    -1000 <= nums[i] <= 1000
    -107 <= k <= 107

"""


class Solution:
    # TC - O(n^2), SC - O(1)
    def subarraySum_brute(self, nums, k) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            curr_sum = 0
            for j in range(i, n):
                curr_sum += nums[j]
                if curr_sum == k:
                    count += 1

        return count

    # TC -  O(n), SC - O(n)
    def subaaraySum_optimal(self, nums, k):
        """
        Idea -  Can't use sliding window as (-)ve value are in nums.
        Use Prefix sum and 'x-k' idea here.
            - map starts with base case 0:1 to tell there exists a subarray with sum 0.
            - if there exists entry of diff('x-k') in mpp, then add that freq to count
            - update mpp by 1 + existing mpp[currSum]
            - return count
        """
        prefixMpp = {0: 1}
        count = currSum = 0
        for num in nums:
            # 'x'
            currSum += num
            # 'x-k'
            diff = currSum - k

            count += prefixMpp.get(diff, 0)
            prefixMpp[currSum] = 1 + prefixMpp.get(currSum, 0)
        return count
