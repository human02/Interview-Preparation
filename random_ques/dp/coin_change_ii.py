"""
Coin Change II
Give an array coins of n integers representing coin denominations.
Your task is to find the number of distinct combinations that sum up to a specified amount of money.
If it's impossible to achieve the exact amount with any combination of coins, return 0.
Single coin can be used any number of times. Return your answer with modulo 109+7.

Example 1:
Input: coins = [2,4,10], amount = 10
Output: 4
Explanation: There are four ways to make the amount 10:
1. 2+2+2+2+2
2. 2+4+4
3. 10
4. 2+2+2+4

Example 2:
Input: coins = [5], amount = 5
Output: 1

Example 3:
Input: coins = [1,2,3,5], amount = 5
Output: 6

Constraints:
1 <= n, coins[i], amount <= 103
All the values of coins are unique.
"""
