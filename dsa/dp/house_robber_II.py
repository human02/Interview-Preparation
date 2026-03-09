"""

House Robber - II (Circular Arrangmement)

A thief needs to rob money in a street. The houses in the street are arranged in a circular manner.
Therefore the first and the last house are adjacent to each other. The security system in the street
is such that if adjacent houses are robbed, the police will get notified.

Given an array of integers "Arr" which represents money at each house, we need to return the maximum
amount of money that the thief can rob without alerting the police.

Example 1:
Input: money = [2, 1, 4, 9]
Output: 10
Explanation:
    [2, 1, 4, 9] The underlined houses would give the maximum loot.
    Note that we cannot loot the 1st and 4th houses together.

Example 2:
Input: money = [1, 5, 2, 1, 6]
Output: 11
Explanation:
    [1, 5, 2, 1, 6] The underlined houses would give the maximum loot.

Example 3:
Input: money = [2,9,8,3,6]
Output: 15
Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses.
The maximum you can rob is nums[1] + nums[4] = 15.

Example 4:
Input: nums = [3,4,3]
Output: 4
Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses.
The maximum you can rob is nums[1] = 4.

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""


class Solution:
    # TC - O(2^n + 2^n), SC - O(n)
    def robHouses_recur(self, money):
        n = len(money)
        arr1 = []  # wont have 1st house
        arr2 = []  # wont have last house

        if n == 1:
            return money[0]

        for i in range(n):
            if i != 0:
                arr1.append(money[i])
            if i != (n - 1):
                arr2.append(money[i])

        def helper(ind, arr):
            if ind == 0:
                return arr[0]
            if ind < 0:
                return 0

            pick, not_pick = 0, 0
            pick = helper(ind - 1, arr)
            not_pick = arr[ind] + helper(ind - 2, arr)

            return max(pick, not_pick)

        ans1 = helper(len(arr1) - 1, arr1)
        ans2 = helper(len(arr2) - 1, arr2)

        return max(ans1, ans2)

if __name__ == "__main__":
    obj = Solution()
    print(obj.robHouses_recur([2, 1, 4, 9]))
    print(obj.robHouses_recur([1, 5, 2, 1, 6]))
    print(obj.robHouses_recur([2, 9, 8, 3, 6]))
    print(obj.robHouses_recur([3, 4, 3]))
