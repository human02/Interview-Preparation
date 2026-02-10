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
            - total odd elements -> nums[n//2]
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

    # TC - O(m+n), SC - O(1)
    def findMedian_better(self, nums1, nums2):
        """
        Idea:
            - We dont need the whole new merged list.
            - Just need the values, based on total count of elements
            - Find necessary indexes of the values, and have a counter.
            - Keep iterating and insert values only when count==required indexes
        """

        n1 = len(nums1)
        n2 = len(nums2)
        n = n1 + n2

        ind2 = n // 2
        ind1 = ind2 - 1

        ind2_ele, ind1_ele = -1, -1
        count = 0

        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                if count == ind1:
                    ind1_ele = nums1[i]
                if count == ind2:
                    ind2_ele = nums1[i]
                count += 1
                i += 1

            else:
                if count == ind1:
                    ind1_ele = nums2[j]
                if count == ind2:
                    ind2_ele = nums2[j]
                count += 1
                j += 1

        while i < n1 and (ind1_ele == -1 or ind2_ele == -1):
            if count == ind1:
                ind1_ele = nums1[i]
            if count == ind2:
                ind2_ele = nums1[i]
            count += 1
            i += 1

        while j < n2 and (ind1_ele == -1 or ind2_ele == -1):
            if count == ind1:
                ind1_ele = nums2[j]
            if count == ind2:
                ind2_ele = nums2[j]
            count += 1
            j += 1

        if n % 2 == 1:
            return float(ind2_ele)
        else:
            return (ind1_ele + ind2_ele) / 2

    # TC - O(log(min(m,n)), SC - O()
    def findMedian_optimal(self, nums1, nums2):
        """
        Idea:
        arr1 = [1,3,4,7,10,12], 6 elements
        arr2 = [2,3,6,15], 4 elements

        - Calculate mid index -> 6+4=10, 10/2=5
        - As both arrays are sorted, we need to find left part only
        - We start by taking 0 elements from arr1 and continue increasing arr1 elements
        - At each time we check if the resultant arr is sorted or not
        - To check sorted:
            - using * as the divider
                           l1   r1
                            |   |
                arr1 =  1 3 4 * 7 10 12
                arr2 =    2 3 * 6 15
                            |   |
                           l2   r2
            - l1 < r2
            - l2 < r1
                - Note:
                    - If l1 or l2 dont exist, then take them as float(-inf)
                    - If r1 or r2 dont exist, then take it as float(inf)
        - No point in linear search but we dont see a BS pattern as only 1 valid pattern
        - We still use Binary Search:
            - high = mid-1 when l1>r2
            - low = mid+1 when l2>r1
        - Once we form a valid symmetric pattern is formed, calc median
            - even -> (max(l1,l2)+max(r1,r2))/2
            - odd -> max(l1,l2)
        - For Odd case, we will have (n1+n2+1)//2 as partition elements = on left elements
        """

        n1, n2 = len(nums1), len(nums2)

        # Binary Search on smaller array
        if n1 > n2:
            return self.findMedian_optimal(nums2, nums1)

        n = n1 + n2
        # Length of left half
        left = (n1 + n2 + 1) // 2

        # Apply binary search
        low, high = 0, n1
        while low <= high:
            # Calculate mid index for nums1
            mid1 = (low + high) // 2

            # Calculate mid index for nums2
            mid2 = left - mid1

            # Calculate l1, l2, r1, and r2
            l1 = nums1[mid1 - 1] if mid1 > 0 else float("-inf")
            r1 = nums1[mid1] if mid1 < n1 else float("inf")
            l2 = nums2[mid2 - 1] if mid2 > 0 else float("-inf")
            r2 = nums2[mid2] if mid2 < n2 else float("inf")

            if l1 <= r2 and l2 <= r1:
                # If condition for finding median is satisfied
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Eliminate the right half of nums1
                high = mid1 - 1
            else:
                # Eliminate the left half of nums1
                low = mid1 + 1
        # Dummy statement
        return 0


if __name__ == "__main__":
    obj = Solution()
    print(obj.findMedian_brute([1, 3], [2]))
    print(obj.findMedian_brute([1, 2], [3, 4]))
    print()
    print(obj.findMedian_better([1, 3], [2]))
    print(obj.findMedian_better([1, 2], [3, 4]))
    print()
    print(obj.findMedian_optimal([1, 4, 7, 10, 12], [2, 3, 6, 15]))
    print(obj.findMedian_optimal([1, 3], [2]))
    print(obj.findMedian_optimal([1, 2], [3, 4]))
