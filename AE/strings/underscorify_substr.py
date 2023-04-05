"""

  Write a function that takes in two strings: a main string and a potential
  substring of the main string. The function should return a version of the main
  string with every instance of the substring in it wrapped between underscores.

  If two or more instances of the substring in the main string overlap each
  other or sit side by side, the underscores relevant to these substrings should
  only appear on the far left of the leftmost substring and on the far right of
  the rightmost substring. If the main string doesn't contain the other string
  at all, the function should return the main string intact.
  
  Sample Input:
    string = "testthis is a testtest to see if testestest it works"
    substring = "test"
  
  Sample Output:
    "_test_this is a _testtest_ to see if _testestest_ it works"

"""


def underscorifySubstring(string, substring):
    locations = collapse(getLocation(string, substring))
    return underscorify(string, locations)


def getLocation(string, substring):
    locations = []
    startIdx = 0
    while startIdx < len(string):
        nextIdx = string.find(substring, startIdx)
        # meaning match found
        if nextIdx != -1:
            locations.append([nextIdx, nextIdx + len(substring)])
            startIdx += 1
        # as if no match then further cases wont also have any match
        else:
            break
    return locations


def collapse(locations):
    if not locations:
        return locations
    collapsedLocations = [locations[0]]
    prev = collapsedLocations[0]
    for i in range(1, len(locations)):
        curr = locations[i]
        # overlap case
        if curr[0] <= prev[1]:
            prev[1] = curr[1]
        else:
            collapsedLocations.append(curr)
            prev = curr
    return collapsedLocations


def underscorify(string, locations):
    locationIdx = 0
    stringIdx = 0
    inBtwn = False
    finalResult = []
    i = 0  # counter used for checking both idxes of a location entry
    while stringIdx < len(string) and locationIdx < len(locations):
        if stringIdx == locations[locationIdx][i]:
            finalResult.append("_")
            inBtwn = not inBtwn
            # increment inBtwn
            if not inBtwn:
                locationIdx += 1
            # keep changing it to check both strt n end idx of an entry
            i = 0 if i == 1 else 1
        finalResult.append(string[stringIdx])
        stringIdx += 1
    # case for last '_'
    if locationIdx < len(locations):
        finalResult.append("_")
    # add rest parts of the original string
    elif stringIdx < len(string):
        finalResult.append(string[stringIdx:])
    # convert list to string
    return "".join(finalResult)


underscorifySubstring("testthis is a testtest to see if testestest it works", "test")
