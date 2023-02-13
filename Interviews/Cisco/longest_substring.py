"""
Rav likes puzzles. One day, he challenged Ansh with a puzzle to find-string thatis the same when read forwards and backwards.
Write an algorithm to find the substring from the given string that is the same when read forwards and backwards.

Input:
The input consists of a string- inputStr, representing the given string for the puzzle.

Output:
From the given string, print a sub-string which is the same when reis forwards and backwards.

Note:
- If there are multiple sub-strings of equal length, choose the lexicographically smallest one.
- If there are multiple sub-strings of different length, choose the one with maximum length.
- If there is no sub-string that is the same when read forwards backwards print "None".
- Sub-string is only valid if its length more than 1.
- Strings only contain uppercase characters (A-Z)

Examples:

Input:
YABCCBAZ

Output:
ABCCBA

Explanation:
Given string is "YABCCBAZ", in this only sub-string which is same when read forward and backward is "ABCCBA".
---

Input:
ABC

Outout
None

Explanation:
Given string is "ABC, and no sub-string is present which is same when read forward and backward.
So, the output is "None'

"""
