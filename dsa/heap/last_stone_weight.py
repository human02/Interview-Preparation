"""

Last Stone Weight

You are given an array of integers stones where stones[i] represents the weight of the ith stone.
We want to run a simulation on the stones as follows:
    At each step, we choose the two heaviest stones, with weight x and y and smash them togethers
    If x == y, both stones are destroyed
    If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
    Continue the simulation until there is no more than one stone remaining.

Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
    We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
    We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
    We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1

Constraints:
    1 <= stones.length <= 20
    1 <= stones[i] <= 100

"""

import heapq


class Solution:
    # TC - O(nlogn) + O(n), SC - O(n)
    def findLastStone(self, stones):

        # creating max-heap of stones
        stones = [-x for x in stones]  # O(n)
        heapq.heapify(stones)  # O(n)

        while len(stones) > 1:  # O(n-1)
            # choosing heaviest and 2nd heaviest stones
            first = heapq.heappop(stones)  # O(log(n))
            second = heapq.heappop(stones)  # O(log(n))

            # Handles all 3 cases, 1st < 2nd not possible as its max PQ
            if second > first:
                heapq.heappush(stones, first - second)  # O(log(n))

        stones.append(0)

        return abs(stones[0])


if __name__ == "__main__":
    obj = Solution()
    print(obj.findLastStone([2, 3, 6, 2, 4]))
    print(obj.findLastStone([1, 2]))
