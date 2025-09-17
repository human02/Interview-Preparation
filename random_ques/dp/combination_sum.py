"""
Combination Sum

Provided with a goal integer target and an array of unique integer candidates, provide a list of
all possible combinations of candidates in which the selected numbers add up to the target.
The combinations can be returned in any order.

A candidate may be selected from the pool an infinite number of times.
There are two distinct combinations if the frequency of at least one of the selected figures differs.

The test cases are created so that, for the given input, there are fewer than 150 possible combinations
that add up to the target. If there is no possible subsequences then return empty vector.

Examples:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation: 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
5 and 2 are candidates, and 5 + 2 = 7.
3 and 4 are candidates, and 3 + 4 = 7.
There are total three combinations.

Input : candidates = [2], target = 1
Output : []
Explanation : There is no way we can choose the candidates to sum up to target.
"""


class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        self.helper(0, [], target, len(candidates), candidates, ans)
        return ans

    def helper(self, ind, curr_list, target, n, arr, ans):
        # Base Case
        if target == 0:
            ans.append(curr_list[:])  # store a copy
            return
        # Base case - negative index or negative target value
        if ind == n or target < 0:
            return

        # Pick current element
        curr_list.append(arr[ind])
        self.helper(ind, curr_list, target - arr[ind], n, arr, ans)
        curr_list.pop()  # delete req for not-pick step

        # Skip current element
        self.helper(ind + 1, curr_list, target, n, arr, ans)

    def combinationSum_memo(self, candidates, target):
        n = len(candidates)
        # dp[(ind, target)] will store list of combinations
        dp = {}

        def helper(ind, target):
            # base case: exact match
            if target == 0:
                return [[]]
            # invalid cases
            if ind == n or target < 0:
                return []

            # If already computed → return
            if (ind, target) in dp:
                return dp[(ind, target)]

            # ---- CHOICE 1: Pick current number ----
            pick = []
            if target >= candidates[ind]:
                for comb in helper(ind, target - candidates[ind]):
                    pick.append([candidates[ind]] + comb)

            # ---- CHOICE 2: Skip current number ----
            skip = helper(ind + 1, target)

            # Save in dp and return
            dp[(ind, target)] = pick + skip
            return dp[(ind, target)]

        return helper(0, target)
