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

if __name__ == "__main__":
    obj = Solution()
    print(obj.findMaxs_brute([4, 0, -1, 3, 5, 3, 6, 8], 3))
    print(obj.findMaxs_brute([20, 25], 2))
    print(obj.findMaxs_brute([1, 3, -1, -3, 5, 3, 6, 7], 3))
