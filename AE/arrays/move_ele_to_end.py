"""

"""

# O(n) time | O(1) space


def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        if array[j] == toMove:
            j -= 1
        elif array[i] == toMove:
            swap(array, i, j)
            i += 1
        else:
            i += 1
    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
