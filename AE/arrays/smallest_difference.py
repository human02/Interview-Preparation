"""

"""
# O(nlog(n) + mlog(m)) - time | O(1) - space


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    i = 0
    j = 0
    smallestDiff = float("inf")
    currentDiff = float("inf")
    smallestPair = []
    while i < len(arrayOne) and j < len(arrayTwo):
        firstNum = arrayOne[i]
        secondNum = arrayTwo[j]
        if firstNum < secondNum:
            currentDiff = secondNum - firstNum
            i += 1
        elif secondNum < firstNum:
            currentDiff = firstNum - secondNum
            j += 1
        else:
            return [firstNum, secondNum]
        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
            smallestPair = [firstNum, secondNum]
    return smallestPair


print(smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]))
