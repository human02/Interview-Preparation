"""

Count Subarrays with Bounded Spread-Length Cost

Given an integer array nums and an integer k, return the number of non-empty subarrays such that
their cost <= k. The cost of a subarray starting at index i and ending at index j is defined as:
    cost(i,j) = (max(nums[i..j]) - max(nums[i..j])*(j-1+1))

Example 1
Input: nums = [1, 3, 2], k = 2
Output: 4

Explanation:
    [1]: (1-1) x 1 = 0 <= 2 (Valid)
    [3]: (3-3) x 1 = 0 <= 2 (Valid)
    [2]: (2-2) x 1 = 0 <= 2 (Valid)
    [1, 3]: (3-1) x 2 = 4 > 2 (Invalid)
    [3, 2]: (3-2) x 2 = 2 <= 2 (Valid)
    [1, 3, 2]: (3-1) x 3 = 6 > 2 (Invalid)
    Total valid: 4

Constraints
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
    0 <= k <=10^14

"""


class Solution:
    # TC - O(n^3), SC - O(1)
    def findCount_brute(self, nums, k):
        """
        Idea:
        - Create all subarray and write helper function to find the cost
        - Keep count of the subarrays satisfying the condition
        """
        n = len(nums)

        def helper(subarr):
            n_subarr = len(subarr)
            return ((max(subarr) - min(subarr)) * n_subarr) <= k

        count = 0
        for i in range(n):
            for j in range(i, n):
                curr_subarr = nums[i : j + 1]
                if helper(curr_subarr):
                    count += 1
        return count

if __name__ == "__main__":
    obj = Solution()
    print(obj.findCount_brute([1, 3, 2], 2))
    print(obj.findCount_brute([99999], 1))
