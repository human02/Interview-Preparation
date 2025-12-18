"""

4. Median of Two Sorted Arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log(m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


Constraints:
    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106

"""


class Solution:
    # TC - O(m+n), SC - O(m+n)
    def findMedian_brute(self, nums1, nums2):
        """
        Idea:
            - merge both arrays to a new array and find the median
            - total even elements -> (nums[n//2]+nums[n//2-1])//2
            - total odd elements -> (nums[n//2]+nums[n//2-1])//2
        """

        merged_nums = []
        n1 = len(nums1)
        n2 = len(nums2)
        i, j = 0, 0

        # Create new merged list
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                merged_nums.append(nums1[i])
                i += 1
            else:
                merged_nums.append(nums2[j])
                j += 1

        while i < n1:
            merged_nums.append(nums1[i])
            i += 1

        while j < n2:
            merged_nums.append(nums2[j])
            j += 1

        if len(merged_nums) % 2 == 0:
            ele1 = merged_nums[len(merged_nums) // 2]
            ele2 = merged_nums[(len(merged_nums) // 2) - 1]
            return (ele1 + ele2) / 2
        else:
            return float(merged_nums[len(merged_nums) // 2])

if __name__ == "__main__":
    obj = Solution()
    print(obj.findMedian_brute([1, 3], [2]))
    print(obj.findMedian_brute([1, 2], [3, 4]))
