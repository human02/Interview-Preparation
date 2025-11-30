"""

Maximum Product Subarray in an Array

Given an integer array nums. Find the subarray with the largest product, and return the product of the elements
present in that subarray. A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
Input: nums = [4, 5, 3, 7, 1, 2]
Output: 840
Explanation: The largest product is given by the whole array itself

Input: nums = [-5, 0, -2]
Output: 0
Explanation: The largest product is achieved with the following subarrays [0], [-5, 0], [0, -2], [-5, 0, -2].

Input: nums = [1, -2, 3, 4, -4, -3]
Output: 144

Constraints:
    1 <= nums.length <= 104
    -10 <= nums[i] <= 10
    -109 <= product of any prefix or suffix of nums <= 109

"""


class Solution:
    def maxProduct_brute(self, nums):
        """
        Finding out all subsequence and then picking the rest
        """
        maxi = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                prod = 1
                for k in range(i, j + 1):
                    prod = nums[k] * prod
                    maxi = max(maxi, prod)
        return maxi

    def maxProduct_better(self, nums):
        """
        Dont need 3 loop and can be done in 2 loops
        """

        maxi = float("-inf")
        for i in range(len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod = nums[j] * prod
                maxi = max(maxi, prod)
        return maxi

    # Function to find the product of elements in maximum product subarray
    def maxProduct_optimal(self, nums):
        """
        Observation based:
        - all (+)ve values
        - even (-)ve values
        - odd (-)ve values --> remove 1 (-)ve, use prefix and suffix variables
        - Handle 0 case
        """

        n = len(nums)

        ans = float("-inf")  # to store the answer

        # Indices to store the prefix and suffix multiplication
        prefix, suffix = 1, 1

        for i in range(n):

            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1

            # update the prefix and suffix multiplication
            prefix *= nums[i]
            suffix *= nums[n - i - 1]

            # store the maximum as the answer
            ans = max(ans, max(prefix, suffix))

        return ans


if __name__ == "__main__":
    # 0  1  2  3  4  5
    nums = [4, 5, 3, 7, 1, 2]
    sol = Solution()
    ans = sol.maxProduct_optimal(nums)
    print("The product of elements in maximum product subarray is:", ans)
