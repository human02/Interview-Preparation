"""

Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the
start and the end time of the ith interval.'intervals' is initially sorted in ascending order by start_i.
You are given another interval newInterval = [start, end].

Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and
also intervals still does not have any overlapping intervals. You may merge the overlapping intervals if needed.
Return intervals after adding newInterval.

Note: Intervals are non-overlapping if they have no common point. For example, [1,2] and [3,4] are non-overlapping,
but [1,2] and [2,3] are overlapping.

Example 1:
Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
Output: [[1,6]]

Example 2:
Input: intervals = [[1,2],[3,5],[9,10]], newInterval = [6,7]
Output: [[1,2],[3,5],[6,7],[9,10]]v

Constraints:
    0 <= intervals.length <= 1000
    newInterval.length == intervals[i].length == 2
    0 <= start <= end <= 1000

"""


class Solution:
    # TC - O(n), SC - O(n)
    def insertInterval(self, intervals, newInterval):
        # Sorting incase the list is not sorted
        intervals.sort(key=lambda x: x[0])

        res = []
        n = len(intervals)
        i = 0

        # Find & Add the intervals before the newInterval
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        """
        Check OVERLAP with `newInterval` if:
        - It starts before or when `newInterval` ends: `intervals[i][0] <= newInterval[1]`
        - It ends after or when `newInterval` starts: `intervals[i][1] >= newInterval[0]`

        Since you already processed all intervals where `intervals[i][1] < newInterval[0]`, 
        you know that any remaining interval satisfies the second condition automatically.

        So you only need to check: **does this interval start before newInterval ends?
        """
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        res.append(newInterval)

        # Add any remiaing intervals
        while i < n:
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":
    obj = Solution()
    assert obj.insertInterval([[1, 3], [4, 6]], [2, 5]) == [[1, 6]]
    print(obj.insertInterval([[1, 3], [4, 6]], [2, 5]))
