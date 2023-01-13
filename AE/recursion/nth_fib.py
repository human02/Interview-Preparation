# O(2^n) time | O(n) space

def getNthfib1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthfib1(n-1) + getNthfib1(n-2)


# O(n) time | O(n) space

def getNthfib2(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthfib2(n-1, memoize) + getNthfib2(n-2, memoize)
        return memoize[n]

 # O(n) time | O(1) space


def getNthfib3(n):
    lastTwo = [0, 1]
    count = 3
    while (count <= n):
        nextVal = lastTwo[0]+lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextVal
        count += 1
    return lastTwo[1] if n > 1 else lastTwo[0]  # edge case
