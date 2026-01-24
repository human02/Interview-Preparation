"""

31. Next Permutation

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr:
    [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1].

The next permutation of an array of integers is the next lexicographically greater permutation of its integers.
More formally, if all the permutations of the array are sorted in lexicographical order, then the next permutation
of that array is the permutation that follows it in the sorted order.

If such arrangement is not possible (i.e., the array is the last permutation), then rearrange it to the lowest possible
order (i.e., sorted in ascending order). You must rearrange the numbers in-place and use only constant extra memory.

Examples:
Input: nums = [1,2,3]
Output: [1,3,2]
Explanation: The next permutation of [1,2,3] is [1,3,2].

Input: nums = [3,2,1]
Output: [1,2,3]
Explanation:[3,2,1] is the last permutation. So we return the first: [1,2,3].

Input: nums = [1,1,5]
Output: [1,5,1]

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 100

"""

# No need to find all permutation and code it. Its N * N! - Bad Solution


# Find Breaking point (ascending from right)
class Solution:
    def find_next(self, s: str) -> str:
        s_list = list(s)
        brk_pt = -1

        # find break point from right
        for i in range(len(s_list) - 2, -1, -1):
            if s_list[i] < s_list[i + 1]:
                brk_pt = i
                break

        # return Descending order if no breakpoint found
        if brk_pt == -1:
            return "".join(reversed(s_list))

        # Find the element just greater than brk_pt element
        for i in range(len(s_list) - 1, brk_pt, -1):
            if s_list[i] > s_list[brk_pt]:
                s_list[i], s_list[brk_pt] = s_list[brk_pt], s_list[i]
                break

        # Reverse the right half to get the next smallest permutation
        s_list[brk_pt + 1 :] = reversed(s_list[brk_pt + 1 :])
        return "".join(s_list)


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_next(""))
    print(obj.find_next("123"))
    print(obj.find_next("321"))
    print(obj.find_next("151"))
    print(obj.find_next("abdc"))
