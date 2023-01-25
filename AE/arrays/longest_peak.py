"""

"""


def longestPeak(array):
    longestPeak = 0
    # strt from idx 1 and check if element is a peak
    i = 1
    while i < len(array) - 1:
        isPeak = array[i] > array[i-1] and array[i] > array[i+1]
    # if not a peak then continue to next idx
        if not isPeak:
            i += 1
            continue
    # if peak, then expand in both direction until decreasing
        # start from nonpeak element on the left
        leftIdx = i-2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx+1]:
            leftIdx -= 1
        # start from nonpeak element on the right
        rightIdx = i+2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx-1]:
            rightIdx += 1
        # once done expanding, compute the length of the current peak
        currPeak = rightIdx - leftIdx - 1
        # store only max of peak lengths
        longestPeak = max(longestPeak, currPeak)
        # we dont want to check the idx as they were part of prev peaks
        i = rightIdx
    return longestPeak
