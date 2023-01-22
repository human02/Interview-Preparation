"""

"""


def mergeOverlappingIntervals(intervals):
    # sort array as we dont know if its sorted
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    # assuming intervals has elements
    # Also we want to add element to a new list and then traverse and keep checking
    # It help in checking the merged element with the next element
    # this way we donot need to expand until overlap not found

    mergedIntervals = []
    currInterval = sortedIntervals[0]
    mergedIntervals.append(currInterval)

    for nextInterval in sortedIntervals:
        # decompressing the indexes
        _, currEnd = currInterval
        nextStart, nextEnd = nextInterval

        if (currEnd >= nextStart):
            currInterval[1] = max(currEnd, nextEnd)
        else:
            currInterval = nextInterval
            mergedIntervals.append(currInterval)

    return mergedIntervals


print(mergeOverlappingIntervals([[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]))
