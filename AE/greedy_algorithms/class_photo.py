"""
"""


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    # Make sure to check for cases when the height are same.
    firstRowColor = "R" if redShirtHeights[0] < blueShirtHeights[0] else "B"
    for i in range(len(redShirtHeights)):
        redHeight = redShirtHeights[i]
        blueHeight = blueShirtHeights[i]
        if firstRowColor == 'R':
            if redHeight >= blueHeight:
                return False
        else:
            if blueHeight >= redHeight:
                return False
    return True


print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))
