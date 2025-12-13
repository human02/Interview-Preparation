"""

2 Sum - Pair Sum Closest to Target

Given an array arr[] of n integers and an integer target, find a pair of elements from the array such that the sum of the pair is closest to the given target.
Note:
    - Return the pair in sorted order.
    - If multiple pairs have the same closest sum, return the one with the maximum absolute difference (i.e., |a - b| is largest).
    - If no valid pair exists (i.e., array has fewer than 2 elements), return an empty array.

Examples:
Input: arr[] = [10, 30, 20, 5], target = 25
Output: [5, 20]
Explanation: Out of all the pairs, [5, 20] has sum = 25 which is closest to 25.

Input: arr[] = [5, 2, 7, 1, 4], target = 10
Output: [2, 7]
Explanation: As (4, 7) and (2, 7) both are closest to 10, but absolute difference of (2, 7) is 5 and (4, 7) is 3. Hence, [2, 7] has maximum absolute difference and closest to target.

Input: arr[] = [10], target = 10
Output: []
Explanation: As the input array has only 1 element, return an empty array.

"""


class Solution:
    #  TC - O(n^2), SC - O(1)
    def findPair_brute(self, arr, target):
        n = len(arr)

        # Edge Case
        if n < 2:
            return []

        minDiff = float("inf")
        result = None
        maxAbsDiff = -1

        for i in range(n):
            for j in range(i + 1, n):
                curr_sum = arr[i] + arr[j]
                curr_diff = abs(target - curr_sum)
                curr_abs_diff = abs(arr[i] - arr[j])

                # Found a closer sum
                if curr_diff < minDiff:
                    minDiff = curr_diff
                    maxAbsDiff = curr_abs_diff
                    result = sorted([arr[i], arr[j]])

                # Same closest sum, check if this pair has larger absolute difference
                elif curr_diff == minDiff and curr_abs_diff > maxAbsDiff:
                    maxAbsDiff = curr_abs_diff
                    result = sorted([arr[i], arr[j]])

        return result if result else []

    #  TC - O(nlog(n)), SC - O(1)
    def findPair_optimal(self, arr, target):
        n = len(arr)
        if n < 2:
            return []

        arr.sort()
        l = 0
        r = n - 1
        minDiff = float("inf")
        result = None
        maxAbsDiff = -1

        while l < r:
            curr_sum = arr[l] + arr[r]
            curr_diff = abs(target - curr_sum)
            curr_abs_diff = arr[r] - arr[l]  # as already in sorted order

            if curr_diff < minDiff:
                minDiff = curr_diff
                maxAbsDiff = curr_abs_diff
                result = sorted([arr[l], arr[r]])

            # Same closest sum, check if this pair has larger absolute difference
            elif curr_diff == minDiff and curr_abs_diff > maxAbsDiff:
                maxAbsDiff = curr_abs_diff
                result = sorted([arr[l], arr[r]])

            if curr_sum < target:
                l += 1
            else:
                r -= 1

        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.findPair_brute(arr=[10, 30, 20, 5], target=25))
    print(obj.findPair_brute(arr=[5, 2, 7, 1, 4], target=10))
    print(obj.findPair_brute(arr=[10], target=10))
    print()
    print(obj.findPair_optimal(arr=[10, 30, 20, 5], target=25))
    print(obj.findPair_optimal(arr=[5, 2, 7, 1, 4], target=10))
    print(obj.findPair_optimal(arr=[10], target=10))
