"""
"""


def largestRange(array):
    # nlog(n)
    array.sort()
    ranges = []

    print(array, "\n")
    # When there is only 1 element then return it as both the value for ranges.
    if len(array) == 1:
        return [array[0], array[0]]

    start = 0
    end = 0
    for i in range(1, len(array)):
        if array[i - 1] == array[i] or array[i - 1] == array[i] - 1:
            end += 1
        else:
            ranges.append([array[start], array[end]])
            start = i
            end = i
    ranges.append([array[start], array[end]])

    result = []
    longest = float("-inf")
    for i in ranges:
        if i[1] - i[0] > longest:
            longest = i[1] - i[0]
            result = i
    return result


# O(n) time | O(n) space
def largestRangeOptimized(array):
    bestRange = []
    # store the longest range length.
    bestLen = 0
    # Stores the nums of the array and has visited criteria as well
    nums = {}

    # traverse and initialize the hashmap
    for i in array:
        nums[i] = True

    for i in array:

        # Skipping this value if already the value is checked for range
        if not nums[i]:
            continue

        # Keep count if val already checked
        nums[i] = False
        currLen = 1

        # checking the left-most range value for i value
        left = i - 1
        while left in nums:
            nums[left] = False
            currLen += 1
            left -= 1

        # checking the right-most range value for i value
        right = i + 1
        while right in nums:
            nums[right] = False
            currLen += 1
            right += 1

        # Add the range if greater than existing best length
        if currLen > bestLen:
            # +1 and -1 as values changes before the while condition is false
            bestRange = [left + 1, right - 1]
            bestLen = currLen

    return bestRange


print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
print(
    largestRange(
        [
            19,
            -1,
            18,
            17,
            2,
            10,
            3,
            12,
            5,
            16,
            4,
            11,
            8,
            7,
            6,
            15,
            12,
            12,
            2,
            1,
            6,
            13,
            14,
        ]
    )
)
print(largestRange([4, 1, 3, 2]))
