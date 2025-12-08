"""

Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence derived from an array by deleting some or no elements without changing
the order of the remaining elements. For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].
The task is to find the length of the longest subsequence in which every element is greater than the previous one.

Examples:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0, 1, 0, 3, 2, 3]
Output: 4
Explanation: The longest increasing subsequence is [0, 1, 2, 3], and its length is 4

Input: nums = [7, 7, 7, 7, 7, 7, 7]
Output:1

Constraints:
    1 <= nums.length <= 105
    -106 <= nums[i] <= 106

"""


class Solution:
    # TC - O(2^n), SC - O(n)
    def LIS_recursive(self, nums):
        n = len(nums)

        def helper(i, prevInd):

            # Base case: reached beyond the array
            if i == len(nums):
                return 0

            # Not take current element
            notTake = helper(i + 1, prevInd)

            # Take current element if valid
            take = 0
            if prevInd == -1 or nums[i] > nums[prevInd]:
                take = 1 + helper(i + 1, i)

            return max(take, notTake)

        return helper(0, -1)

    # TC - O(n^2), SC - O(n^2) + O(n)
    def LIS_memoized(self, nums):
        n = len(nums)

        """
        States for ind => 0 to n-1, 
        prevInd => -1 to n-1, but -1 cnt be index as it points to last index
        hence n+1
        """
        dp = [[-1] * (n + 1) for _ in range(n)]

        # Helper function to find the length of LIS
        def helper(i, prevInd):

            # -> Base case: reached beyond the array
            if i == len(nums):
                return 0

            if dp[i][prevInd] != -1:
                return dp[i][prevInd]

            # Not Take case
            notTake = helper(i + 1, prevInd)

            take = 0  # Take case

            # If no element is chosen till now
            if prevInd == -1 or nums[i] > nums[prevInd]:
                take = 1 + helper(i + 1, i)

            dp[i][prevInd] = max(take, notTake)

            # Return the maximum length obtained from both cases
            return dp[i][prevInd]

        return helper(0, -1)


if __name__ == "__main__":
    obj = Solution()
    print(obj.LIS_recursive([10, 9, 2, 5, 3, 7, 101, 18]))
    print(obj.LIS_recursive([0, 1, 0, 3, 2, 3]))
    print(obj.LIS_recursive([7, 7, 7, 7, 7, 7, 7]))
    print()
    print(obj.LIS_memoized([10, 9, 2, 5, 3, 7, 101, 18]))
    print(obj.LIS_memoized([0, 1, 0, 3, 2, 3]))
    print(obj.LIS_memoized([7, 7, 7, 7, 7, 7, 7]))
