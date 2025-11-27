"""

198. House Robber - I (Straight Arrangement)

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from
robbing each of them is that adjacent houses have security systems connected and it will
automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum
amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 400

"""


class Solution:
    # TC - O(2^n), SC - O(n)
    def robHouses_recur(self, nums):
        n = len(nums)

        def helper(ind):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return float("-inf")

            pick, not_pick = 0, 0
            not_pick = helper(ind - 1)
            pick = nums[ind] + helper(ind - 2)

            return max(pick, not_pick)

        return helper(n - 1)

    # TC - O(n), SC - O(n)
    def robHouses_memo(self, nums):
        n = len(nums)
        dp = [-1] * n

        def helper(ind, dp):
            if ind == 0:
                return nums[0]
            if ind < 0:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            pick, not_pick = 0, 0
            pick = nums[ind] + helper(ind - 2, dp)
            not_pick = helper(ind - 1, dp)

            dp[ind] = max(pick, not_pick)

            return dp[ind]

        return helper(n - 1, dp)

    # TC - O(n), SC - O(n) (removed O(n) used by stack)
    def robHouses_tabu(self, nums):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        neg = 0

        for ind in range(1, n):
            pick = nums[ind]
            if ind > 1:
                pick += dp[ind - 2]
            not_pick = dp[ind - 1]
            dp[ind] = max(pick, not_pick)
        return dp[-1]

    # TC - O(n), SC - O(1)
    def robHouses_spaceOP(self, nums):
        n = len(nums)
        prev = nums[0]
        prev2 = 0

        for ind in range(1, n):
            pick = nums[ind]
            if ind > 1:
                pick += prev2
            not_pick = prev
            curr_i = max(pick, not_pick)
            prev2 = prev
            prev = curr_i
        return prev


if __name__ == "__main__":
    obj = Solution()
    print(obj.robHouses_recur([1, 2, 3, 1]))
    print(obj.robHouses_recur([2, 7, 9, 3, 1]))
    print()
    print(obj.robHouses_memo([1, 2, 3, 1]))
    print(obj.robHouses_memo([2, 7, 9, 3, 1]))
    print()
    print(obj.robHouses_tabu([1, 2, 3, 1]))
    print(obj.robHouses_tabu([2, 7, 9, 3, 1]))
    print()
    print(obj.robHouses_spaceOP([1, 2, 3, 1]))
    print(obj.robHouses_spaceOP([2, 7, 9, 3, 1]))
