"""

Jump Game II

You are given an array of integers nums, where nums[i] represents the maximum length of a jump towards the right from index i.
For example, if you are at nums[i], you can jump to any index i + j where:
    j <= nums[i]
    i + j < nums.length
    You are initially positioned at nums[0].
Return the minimum number of jumps to reach the last position in the array (index nums.length - 1).
You may assume there is always a valid answer.

Example 1:
Input: nums = [2,4,1,1,1,1]
Output: 2
Explanation: Jump from index 0 to index 1, then jump from index 1 to the last index.

Example 2:
Input: nums = [2,1,2,1,0]
Output: 2

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 100

"""


class Solution:
    # TC - O(2^n), SC - O(n)
    def findMin_recur(self, nums):
        n = len(nums)

        def helper(ind):
            if ind == n - 1:
                return 0  # nothing to do as we reached the end
            if ind >= n:  # best value to return for invalid index, finding min
                return float("inf")

            # max index where from this index, we can reach
            endJumpInd = ind + nums[ind]

            # As we are finding min, hence default = inf
            res = float("inf")

            # start from next ind till end Ind
            for i in range(ind + 1, endJumpInd + 1):
                res = min(res, 1 + helper(i))
            return res

        return helper(0)

    # TC - O(n^2), SC - O(n)
    def findMin_memo(self, nums):
        n = len(nums)
        dp = [-1] * n  # As states change from 0 to n-1, n states

        def helper(ind):
            if ind == n - 1:
                return 0  # nothing to do as we reached the end
            if ind >= n:
                return float(
                    "inf"
                )  # best value to return for invalid index as we are finding min

            if dp[ind] != -1:
                return dp[ind]

            res = float("inf")
            endJumpInd = ind + nums[ind]
            # start from next ind till end Ind
            for i in range(ind + 1, endJumpInd + 1):
                res = min(res, 1 + helper(i))
            dp[ind] = res

            return dp[ind]

        return helper(0)

    def findMin_greedy(self, nums):
        n = len(nums)

        # Check for case if 1st element is zero
        if nums[0] == 0:
            return -1

        maxReach = 0
        currReach = 0
        jump = 0
        for i in range(n):
            maxReach = max(maxReach, i + nums[i])

            if maxReach >= n - 1:
                return jump + 1

            # Increment the Jump as we reached the
            # Current Reachable index
            if i == currReach:

                # If Max reach is same as current index
                # then we can not jump further
                if i == maxReach:
                    return -1

                # If Max reach > current index then increment
                # jump and update current reachable index
                else:
                    jump += 1
                    currReach = maxReach

        return -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMin_recur([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_memo([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_greedy([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_recur([2, 1, 2, 1, 0]))
    print(obj.findMin_memo([2, 1, 2, 1, 0]))
    print(obj.findMin_greedy([2, 1, 2, 1, 0]))
