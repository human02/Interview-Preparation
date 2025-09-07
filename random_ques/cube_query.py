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

from bisect import bisect_right
""" edge cases:
 
1. if the budget is less than the price of the first item at pos, correctly returns 0. 

algo:

1. create a prefix sum array 'ps' for O(1) range sum lookups. 
2. iterate over each query (pos 'p', amount 'a'). 
3. calc the 'limit', the max cumulative sum affordable (sum before 'p' + amount 'a'). 
4. use bisect_right on 'ps' to binary search for the furthest affordable index 'r'. 
5. the number of items is the diff between the end index and start index: r - (p - 1). 
6. store the result and return the final list. 
t.c - O(n + q log n) - O(n) to build prefix sums, then O(log n) for each of the q queries. 
s.c - O(n + q) - for the prefix sum array and the answer array. 

"""


from bisect import bisect_right

def findMaximumValue(prices, pos, amount):
    n = len(prices)
    
    # Step 1: Build prefix sum array (1-indexed for convenience)
    # ps[i] = total cost of products from prices[0] to prices[i-1]
    ps = [0] * (n + 1)
    for i, v in enumerate(prices, 1):
        ps[i] = ps[i - 1] + v
    
    ans = []
    
    # Step 2: Process each query (p = starting cubicle, a = available money)
    for p, a in zip(pos, amount):
        # Money already "virtually spent" before position p
        # i.e., prefix sum up to cubicle (p-1)
        base = ps[p - 1]
        
        # Alex can spend at most (base + a) in total
        # This allows us to do a prefix sum lookup in one shot
        limit = base + a
        
        # Binary search: find rightmost index r such that ps[r] <= limit
        # bisect_right returns the insertion point, so subtract 1
        r = bisect_right(ps, limit) - 1
        
        # If r < p-1, it means even the first product at position p is too expensive
        if r < p - 1:
            ans.append(0)
        else:
            # Otherwise, Alex can buy (r - (p-1)) products
            ans.append(r - (p - 1))
    
    return ans
