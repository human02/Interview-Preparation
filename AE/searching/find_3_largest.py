"""

"""


# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    # using None here but ask the interviewer how to initialize it.
    threeLargest = [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    if (threeLargest[2] == None or num > threeLargest[2]):
        slideAndUpdate(threeLargest, num, 2)
    elif (threeLargest[1] == None or num > threeLargest[1]):
        slideAndUpdate(threeLargest, num, 1)
    elif (threeLargest[0] == None or num > threeLargest[0]):
        slideAndUpdate(threeLargest, num, 0)


def slideAndUpdate(array, num, idx):
    for i in range(idx+1):
        if i == idx:
            array[idx] = num
        else:
            array[i] = array[i+1]
