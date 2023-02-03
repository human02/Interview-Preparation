"""

"""


def longestSubstringWithoutDuplication(string):
    # map to store last seen values
    lastSeen = {}

    # Initialising as the atleast the 1st index will be the longest substrng w/o duplicates
    longest = [0, 1]
    startIdx = 0
    for i, char in enumerate(string):
        if char in lastSeen:
            startIdx = max(startIdx, lastSeen[char] + 1)
        # checking if longest < new string
        if longest[1] - longest[0] < i + 1 - startIdx:
            longest = [startIdx, i + 1]
        # update lastSeen irrespective if character present or not in lastSeen
        lastSeen[char] = i

    return string[longest[0] : longest[1]]


print(longestSubstringWithoutDuplication("clementisacap"))
