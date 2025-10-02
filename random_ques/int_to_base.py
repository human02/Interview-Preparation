"""
Convert Integer to Any Base

Description:
Given an integer num and a base base, convert the integer to its string representation in the specified base.
The base can be any integer from 2 to 36. For bases greater than 10, use uppercase letters 'A' through 'Z' to
represent digits 10 through 35. DO NOT Use in-built function.

Example 1:
Input: num = 10, base = 2
Output: "1010"
Explanation: 10 in decimal is 1010 in binary.

Example 2:
Input: num = 255, base = 16
Output: "FF"
Explanation: 255 in decimal is FF in hexadecimal.

Example 3:
Input: num = 123, base = 8
Output: "173"
Explanation: 123 in decimal is 173 in octal.

Example 4:
Input: num = -42, base = 10
Output: "-42"
Explanation: Negative numbers should be prefixed with a minus sign.

Example 5:
Input: num = 0, base = 16
Output: "0"
Explanation: Zero is represented as "0" in any base.

Constraints:
-10^9 <= num <= 10^9
2 <= base <= 36

"""


class Solution:
    def int_to_base(self, num, base):
        res = ""
        # necessary for conversion to str
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num == 0:
            return "0"
        if num < 0:
            isNegative = True
        else:
            isNegative = False

        tmp = abs(num)
        while tmp != 0:
            rem = tmp % base
            res = digits[rem] + res
            tmp //= base
        return res if not isNegative else "-" + res


if __name__ == "__main__":
    obj = Solution()
    print(obj.int_to_base(25, 5))
    print(f"\nTesting Now, If any test case fails then Assertion Error will be raised.")
    assert obj.int_to_base(0, 10) == "0"
    assert obj.int_to_base(25, 5) == "100"
    assert obj.int_to_base(10, 2) == "1010"
    assert obj.int_to_base(255, 16) == "FF"
    assert obj.int_to_base(-42, 10) == "-42"
    assert obj.int_to_base(123, 8) == "173"
    print(f"Congratulations, All Test Cases Passed!\n")
