"""

You are given two integers, lowVal and highVal. A lottery is being held where every integer in the inclusive range [lowVal, highVal] represents a ticket.
Each ticket is assigned a Coupon Code based on the sum of its digits.

For example:
    Ticket 10 has a Coupon Code of 1+0=1.
    Ticket 123 has a Coupon Code of 1+2+3=6.

Participants holding tickets that result in the same Coupon Code share a prize pool.
Your task is to determine two things:The maximum number of winners assigned to any single Coupon Code.
The total number of unique Coupon Codes that achieve this maximum number of winners.
Return these two values as an array or a pair: [max_winners, count_of_codes].

Constraints:
    1 <= lowVal <= highVal <= 10^18

"""


class Solution:
    """
    Idea:
    - Recursive way helps with Memoization
    - While loop way will only check ones and will basically calculate for all numbers
    - To make Memoization truly powerful, you should use the recursive property: sum(123) = 3 + sum(12)
    """

    def findGroup_recur(self, lowVal, highVal):

        def helper(num):
            if num == 0:
                return 0
            return (num % 10) + helper(num // 10)

        mpp = {}
        for i in range(lowVal, highVal + 1):
            mpp[helper(i)] = mpp.get(helper(i), 0) + 1

        maxCount = max(mpp.values())
        res = sum(1 for val in mpp.values() if val == maxCount)

        return [maxCount, res]

    def findGroup_memo(self, lowVal, highVal):

        memo = {}

        def helper(num):
            if num == 0:
                return 0
            if num in memo:
                return memo[num]

            memo[num] = (num % 10) + helper(num // 10)
            return memo[num]

        mpp = {}
        for i in range(lowVal, highVal + 1):
            mpp[helper(i)] = mpp.get(helper(i), 0) + 1

        maxCount = max(mpp.values())
        res = sum(1 for val in mpp.values() if val == maxCount)

        return [maxCount, res]

    def findGroup_spaceOp(self, lowVal, highVal):
        def helper(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        mpp = {}
        for i in range(lowVal, highVal + 1):
            mpp[helper(i)] = mpp.get(helper(i), 0) + 1

        maxCount = max(mpp.values())
        res = sum(1 for val in mpp.values() if val == maxCount)

        return [maxCount, res]


if __name__ == "__main__":
    obj = Solution()
    print(obj.findGroup_recur(1, 13))
    print(obj.findGroup_recur(20, 25))
    print(obj.findGroup_recur(1, 13))
    print(obj.findGroup_recur(20, 25))
