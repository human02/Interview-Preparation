"""

"""
# note any logic that doesn't keeps in mind the order of string is incorrect.


# O(n+m) time | O(n+m) space as we are doing substring and it requires copying
def oneEdit(stringOne, stringTwo):

    len1, len2 = len(stringOne), len(stringTwo)

    # case where strings are different by more than 1
    if abs(len1 - len2) > 1:
        return False

    # Running till the min string index
    for i in range(min(len1, len2)):
        # case where we find an element that is not same in both strings
        # one time is fine and next case wont get to this place
        if stringOne[i] != stringTwo[i]:
            # 1st 2 cases of add/remove
            if len1 > len2:
                return stringOne[i + 1 :] == stringTwo[i:]
            elif len2 > len1:
                return stringOne[i:] == stringTwo[i + 1 :]
            # replace case
            else:
                return stringOne[i + 1 :] == stringTwo[i + 1 :]

    # When both were same strings or 1 of the 2 strings just had 1 character
    return True


# O(n) time where n is the length of shorter string as we end traverse at it
# O(1) space as we are not using substring
def oneEditOptimized(stringOne, stringTwo):

    len1, len2 = len(stringOne), len(stringTwo)

    # case where strings are different by more than 1
    if abs(len1 - len2) > 1:
        return False

    madeEdit = False
    indexOne = 0
    indexTwo = 0

    while indexOne < len1 and indexTwo < len2:
        # case when character is not same
        if stringOne[indexOne] != stringTwo[indexTwo]:
            # If made edit already set that means its second edit and return false
            if madeEdit:
                return False
            else:
                madeEdit = True
            #  now determine which index to increment
            if len1 > len2:
                indexOne += 1
            elif len2 > len1:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        # case when character is same
        else:
            indexOne += 1
            indexTwo += 1

    return True
