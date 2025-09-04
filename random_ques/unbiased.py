"""
Problem: Minimum Operations to Make Two Strings Unbiased

You are given two binary strings data1 and data2, each of length n.

You are allowed to perform the following operations:
	•	Drop some characters from the right end of data1 (possibly zero).
	•	Drop some characters from the left end of data2 (possibly zero).

After dropping, let the resulting strings be s1 and s2.
Concatenate them as s = s1 + s2.

We call the string unbiased if:
	•	The number of '1' characters in s equals the number of '0' characters.
Return the minimum number of operations needed to make the two strings unbiased.


Input: n = 4, data1 = "1010", data2 = "1100"
Output: 2
Explanation:
- Remove 1 character from right of data1 → "101"
- Remove 1 character from left of data2 → "100"
Now condition holds → unbiased with 2 operations.


"""
from typing import List

def minOperationsToUnbias(n: int, data1: str, data2: str) -> int:
    """
        edge cases:
            1. n == 0 -> return 0
            2. strings with all 0s or all 1s -> handled by general logic (may end up dropping many)
        algo:
            1. build prefix sums of '1's for both strings so we can ask
               ones(data1[:k]) and ones(data2[:k]) in O(1)
            2. define for dropping i from RIGHT of data1:
                   a(i) = 2 * ones(data1[:n-i]) + i
               keep the smallest i that gives each a(i) in a hashmap
            3. sweep j from 0..n for LEFT drops on data2:
                   b(j) = 2 * ones(data2[j:]) + j
               to be unbiased, we need a(i) + b(j) == 2n  ==> look up need = 2n - b(j)
            4. track min (i + j) across all matches and return it
        t.c - O(n)  (one pass to build prefix, one pass to build map, one pass to sweep j)
        s.c - O(n)  (prefix arrays + hashmap for a(i))
    """
    # prefix counts of ones
    p1 = [0] * (n + 1)
    p2 = [0] * (n + 1)
    for i in range(n):
        p1[i + 1] = p1[i] + (data1[i] == '1')
        p2[i + 1] = p2[i] + (data2[i] == '1')

    ones2_total = p2[n]

    best_for_a = {}
    for i in range(0, n + 1):
        ones_after_i = p1[n - i]
        a = 2 * ones_after_i + i
        if a not in best_for_a or i < best_for_a[a]:
            best_for_a[a] = i

    ans = 2 * n  
    for j in range(0, n + 1):
        ones2_after_j = ones2_total - p2[j]
        b = 2 * ones2_after_j + j
        need = 2 * n - b
        if need in best_for_a:
            i = best_for_a[need]
            if i + j < ans:
                ans = i + j

    return ans