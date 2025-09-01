"""
You are given an m x n grid of points (not cells). A square is defined as 4 points that form the 
corners of an axis-aligned square.

Write a function to count the total number of axis-aligned squares that can be formed from these points.

m = 2, n = 3
•  •  •
•  •  •

Inptut: m = 2, n = 3
Output: 2
Explanation: We can form 2 squares, each of side length 1.      

Input: m = 3, n = 3
Output: 5
Explanation: We can form 5 squares, 4 of side length 1 and 1 of side length 2.

Input: m = 4, n = 4
Output: 14          

Constraints:
·  1 <= m, n <= 100 

"""

class Solution:
    def countSquares(self, m: int, n: int) -> int:
        total = 0
        # max possible side length
        max_side = min(m, n) - 1  

        for k in range(1, max_side + 1):  # k is side length
            total += (m - k) * (n - k)  
            # explanation: (m-k) choices for rows * (n-k) choices for cols

        return total


# ----------------
# Example runs
# ----------------
if __name__ == "__main__":
    sol = Solution()

    print(sol.countSquares(2, 3))  # Output: 2
    print(sol.countSquares(3, 3))  # Output: 5
    print(sol.countSquares(4, 4))  # Output: 14