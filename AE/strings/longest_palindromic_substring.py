"""
"""

# O(n^3) time | O(n) space


def longestPalindromicSubstring_my_soln(string):
    res = ""
    count = 0
    # case when only one character string
    if len(string) == 1:
        return string

    # now one ptr from start and other from back until we find ith char
    # if found the same char then check if its palindrome
    # likewise store the largest palindrome
    for i in range(len(string)):
        j = len(string) - 1
        while i < j:
            if string[i] == string[j]:
                check = isPalindrome(string, i, j)
                if check:
                    if len(string[i:j+1]) > count:
                        res = string[i:j+1]
                        count = len(string[i:j+1])
            j -= 1
    return res


def isPalindrome(arr, i, j):
    start = i
    end = j
    while (start < end):
        if arr[start] != arr[end]:
            return False
        start += 1
        end -= 1
    return True

# --------------------------------------------------------------------------

# O(n^2) time | O(n) space


def longestPalindromicSubstring(string):
    currLongest = [0, 1]
    for i in range(1, len(string)):
        # getting odd palin case
        odd = getlongestPalinFrom(string, i-1, i+1)
        # getting even palin case
        even = getlongestPalinFrom(string, i-1, i)
        # get the longer palindrome out of the odd and even one
        longest = max(odd, even, key=lambda x: x[1] - x[0])
        # check if new longest is larger and store if thats the case
        currLongest = max(longest, currLongest, key=lambda x: x[1] - x[0])
    return string[currLongest[0]:currLongest[1]]


def getlongestPalinFrom(string, leftIdx, rightIdx):
    # keep loop within the string
    while leftIdx >= 0 and rightIdx < len(string):
        #  break when elements are not same as not palindrome
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
    # as we now are on indexes that break the loop condition,
    # return previous indexes
    return [leftIdx+1, rightIdx]
