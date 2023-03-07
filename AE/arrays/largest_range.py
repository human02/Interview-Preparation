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
