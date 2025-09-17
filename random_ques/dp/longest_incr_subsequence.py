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
    # Helper function to find the length of LIS
    def func(self, i, prevInd, arr):

        # base case
        if i == len(arr) - 1:
            if prevInd == -1 or arr[prevInd] < arr[i]:
                return 1
            return 0

        # Not Take case
        notTake = self.func(i + 1, prevInd, arr)

        take = 0  # Take case

        # If no element is chosen till now
        if prevInd == -1:
            take = self.func(i + 1, i, arr) + 1

        # Else the current element can be
        # taken if it is strictly increasing
        elif arr[i] > arr[prevInd]:
            take = self.func(i + 1, i, arr) + 1

        # Return the maximum length obtained from both cases
        return max(take, notTake)

    # Function to find the longest increasing
    # subsequence in the given array
    def LIS(self, nums):
        return self.func(0, -1, nums)


if __name__ == "__main__":
    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    # Creating an object of Solution class
    sol = Solution()
    lengthOfLIS = sol.LIS(nums)

    print("The length of the LIS for the given array is:", lengthOfLIS)
