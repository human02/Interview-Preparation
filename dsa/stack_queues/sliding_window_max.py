"""

Sliding Window Maximum

Given an array of integers arr, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window

Example 1
Input: arr = [4, 0, -1, 3, 5, 3, 6, 8], k = 3
Output: [4, 3, 5, 5, 6, 8]
Explanation:
Window position        Max
--------------------  -----
[4 0 -1] 3 5 3 6 8      4
4 [0 -1 3] 5 3 6 8      3
4 0 [-1 3 5] 3 6 8      5
4 0 -1 [3 5 3] 6 8      5
4 0 -1 3 [5 3 6] 8      6
4 0 -1 3 5 [3 6 8]      8

For each window of size k=3, we find the maximum element in the window and add it to our output array.

Example 2
Input: arr = [20, 25], k = 2
Output: [25]
Explanation: There’s just one window of size 2 that is possible and the maximum of the two elements is our answer.

Input: arr = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
Output: [3, 3, 5, 5, 6, 7]

Constraints
    1 <= arr.length <= 105
    -104 <= arr[i] <= 104
    1 <= k <= arr.length

"""

from collections import deque


class Solution:
    # TC - O((N-K)*K), SC - O(N-K)
    def findMaxs_brute(self, arr, k):
        n = len(arr)
        ans = []
        for i in range(n - k + 1):
            maxi = arr[i]

            # Traverse the window
            for j in range(i, i + k):
                maxi = max(maxi, arr[j])

            ans.append(maxi)
        return ans

    def findMaxs_optimal(self, arr, k):
        """
        Idea:
        - As the need is to get max in constant time, hence monotonic stack used.
        - monotonic stack is used when constant time min or max value is needed.
        - Keep indexes in the deque
        - keep checking the window
        - remove any element not in decreasing monotonic stack (as max needed)
        - add curr element to deque
        - Confirm if index >=k-1 to create the list
        """
        n = len(arr)
        ans = []
        dq = deque()

        for i in range(n):
            # Update deque to maintain current window
            if dq and dq[0] <= (i - k):
                dq.popleft()

            # Maintain the monotonic (decreasing) order of elements in deque
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()

            # Add current element's index to the deque
            dq.append(i)

            # Store the maximum element from the first window possible
            if i >= (k - 1):
                ans.append(arr[dq[0]])

        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMaxs_brute([4, 0, -1, 3, 5, 3, 6, 8], 3))
    print(obj.findMaxs_brute([20, 25], 2))
    print(obj.findMaxs_brute([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print()
    print(obj.findMaxs_optimal([4, 0, -1, 3, 5, 3, 6, 8], 3))
    print(obj.findMaxs_optimal([20, 25], 2))
    print(obj.findMaxs_optimal([1, 3, -1, -3, 5, 3, 6, 7], 3))
