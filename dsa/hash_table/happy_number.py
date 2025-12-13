"""

202. Happy Number

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which
does not include 1. Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:
Input: n = 19
Output: true
Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

Example 2:
Input: n = 2
Output: false

Constraints:
    0 <= n <= 231 - 1

"""


class Solution:
    # TC - O(n), SC - O(n)
    def isHappy_brute(self, n: int) -> bool:
        visited = set()

        if n == 0:
            return False

        while n not in visited:
            visited.add(n)
            n = self.helper_calSum(n)
            if n == 1:
                return True
        return False

    def helper_calSum(self, num: int) -> int:
        total = 0
        while num:
            digit = num % 10
            total += digit**2
            num //= 10
        return total

    def isHappy_optimal(self, n):
        """
        Idea is that we need to detect cycle using slow and fast pointer.
        """

        slow = n
        fast = n

        while True:
            slow = self.helper_calSum(slow)
            fast = self.helper_calSum(self.helper_calSum(fast))

            # Found 1, it's happy!
            if fast == 1:
                return True
            # Cycle detected, not happy!
            if slow == fast:
                return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.isHappy_brute(19))
    print(obj.isHappy_brute(2))
    print(obj.isHappy_brute(0))
    print()
    print(obj.isHappy_optimal(19))
    print(obj.isHappy_optimal(2))
    print(obj.isHappy_brute(0))
