"""

  Write a function that takes in a string of lowercase English-alphabet letters
  and returns the index of the string's first non-repeating character.
  The first non-repeating character is the first character in a string that
  occurs only once.

  If the input string doesn't have any non-repeating characters, your function
  should return -1.

  Input:
    string = "abcdaf"

  Output:
    1
"""
# O(n^2) - time | O(1) - space


def firstNonRepeatingCharacterBrute(string):
    # brute method
    # both loop from 0 index and check for ith ele
    # check if not the same index
    for i in range(len(string)):
        isPresent = False
        for j in range(len(string)):
            if string[i] == string[j] and i != j:
                isPresent = True
        if not isPresent:
            return i
    return -1


# O(n) - time | O(1) - space as at max dict will have 26 entries and n can be any number hence space is only O(1)


def firstNonRepeatingCharacter(string):
    d = {}
    for i in string:
        # d.get(i,0) gives d[i] if present else gives out 0
        d[i] = d.get(i, 0) + 1

    for i in range(len(string)):
        if d[string[i]] == 1:
            return i
    return -1
