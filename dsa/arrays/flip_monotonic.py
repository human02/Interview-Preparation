"""

Given an array of 0s and 1s. Perform flip operations to make it monotonic.
Return the minimum operation needed to do it.

1s can be flipped to 0s and vice-versa.

Example 1:
Input: arr = [0,0,0,1,1,0]
Output: 1
Explanation: We flip the last 0 to a 1.

Example 2:
Input: arr = [0,0,0,1,1,1]
Output: 0

Example 3:
Input: arr = [1,1,1,0,0,0]
Output: 3

Example 4:
Input: arr = [1,0,0,0,0,0]
Output: 1

Constraints:
    Only 0 or 1 in the array

"""


class Solution:
    # TC - O(n^2), SC - O(1)
    def flipToMonotonic_brute(self, arr):
        """
        Idea:
        - The idea is to see every index as a split point.
        - We want to keep 0s on left of the arr and 1s on the right of the split.
        - We check at each index (a possible split):
            - The number of 1s in the left of the split
                - As we will want to flip them
            - The number of 0s in the right of the split
                - As we will want to flip them
            - Sum these 2 counts and track with a minimum_counter.
        - Minimum count is the answer
        """
        n = len(arr)

        # count 1s on the left of split
        def helper_CountBefore(idx):
            result = 0
            for i in range(idx):
                if arr[i] == 1:
                    result += 1
            return result

        # count 0s on the left of split
        def helper_CountAfter(idx):
            result = 0
            for i in range(idx, n):
                if arr[i] == 0:
                    result += 1
            return result

        minOperation = float("inf")
        # Last index is also a potential split
        for i in range(n + 1):
            leftOnes, rightZeros = 0, 0
            leftOnes = helper_CountBefore(i)
            rightZeros = helper_CountAfter(i)

            currOperation = leftOnes + rightZeros
            minOperation = min(minOperation, currOperation)

        return minOperation

    def flipToMonotonic_optimal(self, arr):
        """
        Idea:
        - We are re-checking the arr for 1s and 0s at each split again.
        - We dont need to do it.
        - Prefix will store how many 1s we have encountered at each split pt.
        - Maintain a running count of 1s and a var for flips.
        - Iterate through each num:
            - Add to 1s count if 1 is seen
            - If 0 is seen:
                - either we flip it, flip +=1
                - or we keep it and flip all the 1s encountered yet
            - We find the minimum of these two operation
        """
        onesCount = 0
        flips = 0  # flip is a potential flip if 0 found later

        for num in arr:
            if num == 1:
                onesCount += 1
            else:  # 0 found
                # flip this 0
                # keep this 0 and flip all prev 1s
                flips = min(flips + 1, onesCount)
        return flips


if __name__ == "__main__":
    obj = Solution()
    print(obj.flipToMonotonic_brute([0, 0, 0, 1, 1, 0]))
    print(obj.flipToMonotonic_brute([0, 0, 0, 1, 1, 1]))
    print(obj.flipToMonotonic_brute([1, 1, 1, 0, 0, 0]))
    print(obj.flipToMonotonic_brute([1, 0, 0, 0, 0, 0]))
    print()
    print(obj.flipToMonotonic_optimal([0, 0, 0, 1, 1, 0]))
    print(obj.flipToMonotonic_optimal([0, 0, 0, 1, 1, 1]))
    print(obj.flipToMonotonic_optimal([1, 1, 1, 0, 0, 0]))
    print(obj.flipToMonotonic_optimal([1, 0, 0, 0, 0, 0]))
