"""
Largest rectangle in a histogram

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1
return the area of the largest rectangle in the histogram.

Examples:
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: The largest rectangle is highlighted, which has an area of 5*2 = 10 units.

Input: heights = [3, 5, 1, 7, 5, 9]
Output: 15
Explanation: The largest rectangle has an area of 5*3 = 15 units.

Input: heights = [2,4]
Output: 4

Constraints:
  1 <= heights.length <= 105
  0 <= heights[i] <= 104

"""


class Solution:
    """
    Idea is to find next smallest and prev smallest for each index.
    Because the smaller limit restricts the rectangle.
    """

    def findNSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []

        for i in range(n - 1, -1, -1):
            # Pop the elements in the stack until the stack is not empty and the top element is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            # Update the answer
            if st:
                ans[i] = st[-1]
            else:
                ans[i] = n

            # Push the index of current element in the stack
            st.append(i)
        return ans

    # Function to find the indices of previous smaller elements
    def findPSE(self, arr):
        n = len(arr)
        ans = [0] * n
        st = []

        for i in range(n):
            # Pop the elements in the stack until the stack is not empty and the top elements is not the smaller element
            while st and arr[st[-1]] >= arr[i]:
                st.pop()

            # Update the answer
            if st:
                ans[i] = st[-1]
            else:
                ans[i] = n

            # Push the index of current element in the stack
            st.append(i)
        return ans

    # Function to find the largest rectangle area
    def largestRectangleArea(self, heights):
        nse = self.findNSE(heights)
        pse = self.findPSE(heights)

        largestArea = 0
        area = 0

        for i in range(len(heights)):
            # Calculate current area
            area = heights[i] * (nse[i] - pse[i] - 1)
            largestArea = max(largestArea, area)
        return largestArea


# Example usage
if __name__ == "__main__":
    heights = [2, 1, 5, 6, 2, 3]
    sol = Solution()
    # Function call to find the largest rectangle area
    ans = sol.largestRectangleArea(heights)
    print("The largest rectangle area is:", ans)
