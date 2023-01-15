"""

"""
# O(n) time | O(1)


def isMonotonic(array):
    # check direction
    isDec = directionHelper(array)
    print(array, isDec)

    # isDec is None when empty or all values are same (this is also monotonic)
    if isDec is None:
        return True
    # Else look for case when the pattern breaks to return False
    else:
        i = 1
        while i < len(array):
            if isDec == True and array[i-1] < array[i]:
                return False
            elif isDec == False and array[i-1] > array[i]:
                return False
            i += 1
        # If no case of pattern breaek is found then return True
        return True


def directionHelper(array):
    i = 1
    isDec = None
    while i < len(array):
        if array[i] != array[i-1] and array[i] < array[i-1]:
            isDec = True
            # return is must else the value will be over- written by
            # after first check is done by seqsequent results.
            return isDec

        elif array[i] != array[i-1] and array[i] > array[i-1]:
            isDec = False
            return isDec
        i += 1
