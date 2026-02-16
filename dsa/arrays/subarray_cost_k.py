"""

Count Subarrays with Bounded Spread-Length Cost

Given an integer array nums and an integer k, return the number of non-empty subarrays such that
their cost <= k. The cost of a subarray starting at index i and ending at index j is defined as:
    cost(i,j) = (max(nums[i..j]) - max(nums[i..j])*(j-1+1))

Example 1
Input: nums = [1, 3, 2], k = 2
Output: 4

Explanation:
    [1]: (1-1) x 1 = 0 <= 2 (Valid)
    [3]: (3-3) x 1 = 0 <= 2 (Valid)
    [2]: (2-2) x 1 = 0 <= 2 (Valid)
    [1, 3]: (3-1) x 2 = 4 > 2 (Invalid)
    [3, 2]: (3-2) x 2 = 2 <= 2 (Valid)
    [1, 3, 2]: (3-1) x 3 = 6 > 2 (Invalid)
    Total valid: 4

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
    0 <= k <=10^14

"""

from collections import deque


class Solution:
    # TC - O(n^3), SC - O(1)
    def findCount_brute(self, nums, k):
        """
        Idea:
        - Create all subarray and write helper function to find the cost
        - Keep count of the subarrays satisfying the condition
        """
        n = len(nums)

        def helper(subarr):
            n_subarr = len(subarr)
            return ((max(subarr) - min(subarr)) * n_subarr) <= k

        count = 0
        for i in range(n):
            for j in range(i, n):
                curr_subarr = nums[i : j + 1]
                if helper(curr_subarr):
                    count += 1
        return count

    # TC - O(n^2), SC - O(1)
    def findCount_better(self, nums, k):
        """
        Idea:
        - Use Sliding Window/2-Pointers, left and right.
            - once, at a length the cost is invalid, then higher length check is waste.
            - no point expanding the subarray and we can shrink it from left.
            - Its due to monotonicity of length and (max-min) both

        - We traverese right < n
            - Dont make it a valid check as it will not consider INTRA valid subarrays
            - In sliding window, when you find a valid window, from left to right
                - num of new valid subarrays = Window size = (r-l+1)
            - Instead, make it 'while its invalid, move left'
            -
        """
        n = len(nums)
        left, right = 0, 0

        def helper(subarr):
            n_subarr = len(subarr)
            return ((max(subarr) - min(subarr)) * n_subarr) <= k

        count = 0
        while right < n:
            while left <= right and not helper(nums[left : right + 1]):
                left += 1
            count += right - left + 1
            right += 1

        return count

    # TC - O(n), SC - O(n)
    def findCount_optimal(self, nums, k):
        """
        Idea:
        - We still need to work on improving the max/min finding.
        - Helper fn is the bottleneck as it rescans the whole subarray.
        - Just changing the inner while to if wont work, it works only for maximum subarray finding.
        - MONOTONIC DEQUE to the rescue
            - It allows for O(1) to find maximum and minimum of a sliding window instead of O(1)
            - Maintain 2 deque - MAXQ and MINQ to store indices for checking if present in window.
            - maxQ:
                - Instead of storing every num, only store potential candidates for curr or future windows.
                - When adding a new number:
                    - If num > maxQ[-1], these can never be max hence pop them.
                - When window shrinking:
                    - if index at front of dequeis the one that was moved past, pop it off.
                - Constant work due to move from front and back.
        - When right is moved forward, add the num to both deque.
        - cost = (nums[maxQ[0]] - nums[minQ[0]]) * (j - i + 1)
        """
        n = len(nums)
        left, right = 0, 0
        maxQ = deque()
        minQ = deque()

        count = 0
        while right < n:
            while maxQ and nums[maxQ[-1]] <= nums[right]:
                maxQ.pop()
            maxQ.append(right)

            while minQ and nums[minQ[-1]] >= nums[right]:
                minQ.pop()
            minQ.append(right)

            while left <= right:  # we need to check intra subarrays
                curr_max = nums[maxQ[0]]
                curr_min = nums[minQ[0]]
                window_len = right - left + 1

                if (curr_max - curr_min) * window_len > k:
                    if maxQ[0] == left:
                        maxQ.popleft()
                    if minQ[0] == left:
                        minQ.popleft()
                    left += 1

                else:  # Valid window
                    break

            count += right - left + 1
            right += 1

        return count


if __name__ == "__main__":
    obj = Solution()
    print(obj.findCount_brute([1, 3, 2], 2))
    print(obj.findCount_brute([99999], 1))
    print(obj.findCount_brute([0], 0))
    print(obj.findCount_brute([5, 4, 3, 2, 1], 10))
    print(obj.findCount_brute([1, 1, 1, 1], 0))
    print()
    print(obj.findCount_better([1, 3, 2], 2))
    print(obj.findCount_better([99999], 1))
    print(obj.findCount_better([0], 0))
    print(obj.findCount_better([5, 4, 3, 2, 1], 10))
    print(obj.findCount_better([1, 1, 1, 1], 0))
    print()
    print(obj.findCount_optimal([1, 3, 2], 2))
    print(obj.findCount_optimal([99999], 1))
    print(obj.findCount_optimal([0], 0))
    print(obj.findCount_optimal([5, 4, 3, 2, 1], 10))
    print(obj.findCount_optimal([1, 1, 1, 1], 0))
