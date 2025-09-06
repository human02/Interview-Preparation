"""
Alex is shopping at Ozone Galleria, where each cubicle sells products at a fixed price.
The cubicles are arranged so that prices are in non-decreasing order from left to right.

There is an array of n integers, prices, where prices[i] is the price of the product at the ith cubicle and q queries
to process. For every query you are given:
- pos: Alex's initial position
- amount: the amount of money Alex has

Alex visit each cubicle starting from pos to n and can purchase max of one product (atmost) from each cubicle visited. 
Determine the maximum number of products Alex can buy without exceeding the available amount.

Example:
Input: prices = [3,4,5,5,7], queries = [[2,10],[1,24],[5,5]]
Output: [2,5,0]
Explanation:
Query 1: Start at cubicle 2 (price = 4), with amount = 10
- Buy at cubicle 2 (4), remaining = 6
- Skip cubicle 3 (5), remaining = 1
- Cannot buy further
=> 2 products

Query 2: Start at cubicle 1 (3), with amount = 24
- Buy [3,4,5,5,7] sequentially
=> 5 products

Query 3: Start at cubicle 5 (7), with amount = 5
- Cannot buy anything
=> 0 products
"""

from typing import List, Tuple 
