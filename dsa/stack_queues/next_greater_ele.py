"""
Next Greater Element

Given an array arr of size n containing elements, find the next greater element for each element in the array
in the order of their appearance. The next greater element of an element in the array is the nearest element
on the right that is greater than the current element. If there does not exist a next greater element for the
current element, then the next greater element for that element is -1.

Examples:
Input: arr = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: In the array, the next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4 is -1,
since it does not exist.

Input: arr = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: In the array, the next larger element to 6 is 8, for 8 there is no larger elements hence
it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on the right and hence -1.

Input: arr = [1, 3, 2]
Output: [3, -1, -1]

Constraints:
  1 ≤ n ≤ 105
  0 ≤ arr[i] ≤ 109
"""


class Solution:
    # TC - O(n^2); SC - O(n)
    def find_next_greater_brute(self, arr):
        n = len(arr)
        ans = [-1] * n
        for i in range(n):
            for j in range(i, n):
                if arr[j] > arr[i]:
                    ans[i] = arr[j]
                    break
        return ans

    # TC - O(n) + O(n) = O(n); SC - O(n)
    def find_next_greater_optimal(self, arr):
        n = len(arr)
        ans = [-1] * n
        # to store the next last greater element
        st = []
        # traverse from the back
        for i in range(n - 1, -1, -1):
            while st:
                if st[-1] > arr[i]:
                    ans[i] = st[-1]
                    break
                else:
                    st.pop()
            st.append(arr[i])
        return ans


if __name__ == "__main__":
    obj = Solution()
    print(obj.find_next_greater_brute([1, 3, 2, 4]))
    print(obj.find_next_greater_brute([6, 8, 0, 1, 3]))
    print(obj.find_next_greater_brute([1, 3, 2]))
    print(f"{"-"*20}")
    print(obj.find_next_greater_optimal([1, 3, 2, 4]))
    print(obj.find_next_greater_optimal([6, 8, 0, 1, 3]))
    print(obj.find_next_greater_optimal([1, 3, 2]))
