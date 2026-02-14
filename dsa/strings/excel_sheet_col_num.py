"""

171. Excel Sheet Column Number

Given a string columnTitle that represents the column title as appears in an Excel sheet,
return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701

Constraints:
    1 <= columnTitle.length <= 7
    columnTitle consists only of uppercase English letters.
    columnTitle is in the range ["A", "FXSHRXW"].

"""


class Solution:
    # TC - O(n), SC - O(1)
    def convertToNum(self, columnTitle):
        """
        Idea:
        - think of it first in base 10:
            - 1234 to number will be:
                - (0*10) + 1 = 1
                - (1*10) + 2 = 12
                - (12*10) + 3 = 123
                - (123*10) + 4 = 1234
            - So its result = 0, then result=result*10 and then result+=s[i]
        - Now we translate it to base 26 (as only Uppercase characters)
        - result = 0, result = result*26, result += ord(s[i]) - ord('A') + 1
        """

        result = 0
        for _, val in enumerate(columnTitle):
            result = result * 26
            result += ord(val) - ord("A") + 1
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.convertToNum("A"))
    print(obj.convertToNum("AB"))
    print(obj.convertToNum("ZY"))
