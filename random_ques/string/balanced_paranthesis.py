"""
Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid and return true if the string is balanced otherwise return false.

Input: str = “()[{}()]”
Output: True
Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order hence they are balanced.

Input: str = “[()”
Output: False
Explanation: As ‘[‘ does not have ‘]’ hence it is not valid and will return false.
"""


class Solution:
    def isValid(self, str: str) -> bool:
        # stack to store brackets
        st = []

        # Inner function to check brackets
        def isSameType(opn, clsd):
            if (
                (opn == "(" and clsd == ")")
                or (opn == "{" and clsd == "}")
                or (opn == "[" and clsd == "]")
            ):
                return True
            return False

        for i in str:
            # push only open brackets to Stack
            if i == "(" or i == "{" or i == "[":
                st.append(i)
            else:
                # check stack, if empty = open brackets over, hence False
                if not st:
                    return False
                # check for bracket type mismatch
                if not isSameType(st.pop(), i):
                    return False

        # String traversed, but open brackets remaining in stack
        if st:
            return False
        # All hurdles passed!
        return True
