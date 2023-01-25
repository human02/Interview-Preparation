
"""
"""


def zeroSumSubarray(nums):

    # the idea is to store sum at each index,
    # if we see a sum again then it means the interim elements sum to 0

    # as 1st index will have sum = 0 as no element are present before that.
    sum = 0

    # using set to store sum values(we do not need indexes) else use diff DS.
    sums = {0}
    for i in nums:
        sum += i
        if sum in sums:
            return True
        else:
            sums.add(sum)
    return False
