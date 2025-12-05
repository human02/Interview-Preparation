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
            # nothing to do as we reached the end
            if ind == n - 1:
                return 0

            # best value to return for invalid index as we are finding min
            if ind >= n:
                return float("inf")

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

    """
    From all positions I can reach with one more jump, which one lets me go farthest?
    """

    def findMin_greedy(self, nums):
        n = len(nums)

        # check - If only 1 element in nums
        if n == 1:
            return 0

        # Check for case if 1st element is zero
        if nums[0] == 0:
            return -1

        maxReach = 0  # Farthest index reachable with one more jump
        currReach = 0  # Farthest index reachable with current jumps, tells when to jump
        jump = 0  # Number of jumps made

        for i in range(n):
            # Update maxReach: from position i, we can reach i + nums[i]
            maxReach = max(maxReach, i + nums[i])

            # If we can already reach the end, return jumps + 1
            if maxReach >= n - 1:
                return jump + 1

            # When we reach the end of current jump range
            if i == currReach:
                # Check if we're stuck (can't jump further)
                if i == maxReach:
                    return -1

                # Make a jump: move to the next range
                else:
                    jump += 1
                    currReach = maxReach  # Update current range to max reachable
        return -1


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMin_recur([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_memo([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_greedy([2, 4, 1, 1, 1, 1]))
    print(obj.findMin_recur([2, 1, 2, 1, 0]))
    print(obj.findMin_memo([2, 1, 2, 1, 0]))
    print(obj.findMin_greedy([2, 1, 2, 1, 0]))
