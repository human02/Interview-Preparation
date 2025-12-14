"""

162. Find peak element

Given an array arr of integers. A peak element is defined as an element greater than both of its neighbors.
Formally, if arr[i] is the peak element, arr[i - 1] < arr[i] and arr[i + 1] < arr[i].

Find the index(0-based) of a peak element in the array. If there are multiple peak numbers,
return the index of any peak number.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly
greater than a neighbor that is outside the array. You must write an algorithm that runs in O(log n) time.

Note:
As there can be many peak values, "true" is given as output if the returned index is a peak number, otherwise "false".

Examples:
Input : arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
Output: 7
Explanation: In this example, there is only 1 peak that is at index 7.

Input : arr = [1, 2, 1, 3, 5, 6, 4]
Output: 1
Explanation: In this example, there are 2 peak numbers at indices 1 and 5. We can consider any of them.

Input : arr = [-2, -1, 3, 4, 5]
Output: 5

Constraints:
    1 <= arr.length <= 1000
    -231 <= arr[i] <= 231 - 1
    arr[i] != arr[i + 1] for all valid i.
    For arr[0], its left element can be considered as -∞
    For arr[n-1], its right element can be considered as -∞

"""


class Solution:
    # TC - O(n), SC - O(1)
    def findPeak_brute(self, nums):
        n = len(nums)

        # Edge case: single element
        if n == 1:
            return 0

        # Check first element
        if nums[0] > nums[1]:
            return 0

        # Check last element
        if nums[n - 1] > nums[n - 2]:
            return n - 1

        for i in range(1, n - 1):
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
                return i

        return -1

if __name__ == "__main__":
    obj = Solution()
    print(obj.findPeak_brute([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
    print(obj.findPeak_brute([1, 2, 1, 3, 5, 6, 4]))
    print(obj.findPeak_brute([-2, -1, 3, 4, 5]))
