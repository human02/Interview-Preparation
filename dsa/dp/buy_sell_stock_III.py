"""

Best Time to Buy and Sell Stock - III

Given an array arr of n integers, where arr[i] represents price of the stock on the ith day.
Determine the maximum profit achievable by buying and selling the stock AT MOST 2 transactions in total.

Holding at most one share of the stock at any time is allowed, meaning buying and selling the stock twice is
permitted, but the stock must be sold before buying it again. Buying and selling the stock on the same day is allowed.

Examples:
Input: arr = [10, 7, 5, 8, 11, 9]
Output: 6
Explanation: Buy on day 3 (price = 5) and sell on day 5 (price = 11), profit = 11 - 5 = 6.

Input: arr = [5, 4, 3, 2, 1]
Output: 0
Explanation: In this case, no transactions are made. Therefore, the maximum profit remains 0.

Input: arr = [3, 8, 1, 4, 6, 2]
Output: 5

Constraints:
    1 <= n<= 10^5
    0 <= arr[i] <= 10^6

"""

class Solution:
    def stockBuySell_recur(self, arr):
        n = len(arr)

        def helper(ind, buy, cap):
            if ind == n or cap == 0:
                return 0

            profit = 0
            if buy == 1:
                profit = max(
                    0 + helper(ind + 1, 1, cap), -arr[ind] + helper(ind + 1, 0, cap)
                )
            else:
                profit = max(
                    0 + helper(ind + 1, 0, cap), arr[ind] + helper(ind + 1, 1, cap - 1)
                )
            return profit

        return helper(0, 1, 2)
if __name__ == "__main__":
    obj = Solution()
    print(obj.stockBuySell_recur([4, 2, 7, 1, 11, 5]))
    print(obj.stockBuySell_recur([5, 7, 2, 10, 6, 9]))
