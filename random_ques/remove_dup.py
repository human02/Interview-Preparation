"""
LeetCode Style Question: Remove Duplicates from Array

Given an integer array nums, remove all duplicate elements in-place such that each element appears only once and return the new length. 
You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return length = 5, with the first five elements of nums being 0, 1, 2, 3, and 4.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""

def removeDuplicates(nums):
    """
    Removes duplicates in-place from sorted array nums.
    Returns the length of the array after duplicates are removed.
    """
    # Edge case: if the input list is empty, return an empty list
    if not nums:
        return []

    # i is the "slow pointer" — it marks the position of the last unique element found
    i = 0  

    # j is the "fast pointer" — it scans through the array
    for j in range(1, len(nums)):
        # If the current element nums[j] is different from the last unique nums[i],
        # we have found a new unique element
        if nums[j] != nums[i]:
            i += 1                  # move slow pointer forward
            nums[i] = nums[j]       # place the unique element at position i

    # At this point, all unique elements are in nums[0..i]
    # Return only the unique portion of the array
    return nums[:i+1]


# Test cases
if __name__ == "__main__":
    nums1 = [1,1,2]
    k1 = removeDuplicates(nums1)
    print(k1, nums1[:k1])  # Output: 2 [1, 2]

    nums2 = [0,0,1,1,1,2,2,3,3,4]
    k2 = removeDuplicates(nums2)
    print(k2, nums2[:k2])  # Output: 5 [0, 1, 2, 3, 4]

    nums3 = [1]
    k3 = removeDuplicates(nums3)
    print(k3, nums3[:k3])  # Output: 1 [1]

    nums4 = []
    k4 = removeDuplicates(nums4)
    print(k4, nums4[:k4])  # Output: 0 []
