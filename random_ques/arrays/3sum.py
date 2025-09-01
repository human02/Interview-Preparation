"""
3 Sum
Given an integer array nums, return all the triplets:
- [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k
- nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
One element can be a part of multiple triplets. The output and the triplets can be returned in any order.

Input: nums = [2, -2, 0, 3, -3, 5]
Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]
Explanation: nums[1] + nums[2] + nums[0] = 0
nums[4] + nums[1] + nums[5] = 0
nums[4] + nums[2] + nums[3] = 0


Input: nums = [2, -1, -1, 3, -1]
Output: [[-1, -1, 2]]
Explanation: nums[1] + nums[2] + nums[0] = 0
Note that we have used two -1s as they are separate elements with different indexes
But we have not used the -1 at index 4 as that would create a duplicate triplet

Input: nums = [8, -6, 5, 4]
(Give answer with the output and triplets sorted in ascending order)
Output:
[]
"""


# OPTIMAL SOLUTION --> O(NlogN)+O(N2) TIME | O(1) SPACE
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        triplets = []
        nums.sort()
        for i in range(n):
            fixed = nums[i]
            # handle duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, n - 1
            while l < r:
                total = fixed + nums[l] + nums[r]
                if total == 0:
                    triplets.append([fixed, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates for l and r
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return triplets


class Solution:
    # Function to find triplets having sum equals to 0
    def threeSum(self, nums):
        # Set to store unique triplets
        triplet_set = set()
        n = len(nums)
        # Check all possible triplets
        for i in range(n):
            # Set to store elements seen so far in the loop
            hashset = set()
            for j in range(i + 1, n):
                # Calculate the 3rd element needed to reach target
                third = -(nums[i] + nums[j])

                """ Find if third element exists in
                 hashset (complements seen so far)"""
                if third in hashset:
                    # Found a triplet that sums up to target
                    temp = [nums[i], nums[j], third]

                    """ Sort the triplet to ensure
                    uniqueness when storing in set"""
                    temp.sort()
                    triplet_set.add(tuple(temp))

                """ Insert the current element 
                into hashset for future checks"""
                hashset.add(nums[j])

        # Convert set to list of lists (unique triplets)
        ans = [list(triplet) for triplet in triplet_set]

        # Return the ans
        return ans


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, -2, 0, 3, -3, 5], [[-3, 0, 3], [-3, 2, 1], [-2, 0, 2]]),
        ([2, -1, -1, 3, -1], [[-1, -1, 2]]),
        ([8, -6, 5, 4], []),
    ]
    for s, expected in test_cases:
        result = sol.threeSum(s)
        print(f"\nInput: {s}\nOutput: {result}\nExpected: {expected}\n")
