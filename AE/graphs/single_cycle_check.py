"""

"""

# key ideas:
# - all elements must be visited + back to start idx + no multiple cycle(s), then only true
# - if not back to starting point after len(array) visited nodes, then false - no cycle
# - if back to starting point but visited < len(array) nodes, then false - multiple cycles


def hasSingleCycle(array):
    # ask interviewer about the starting point
    STARTING_INDEX = 0
    currentIdx = STARTING_INDEX
    numVisited = 0
    while (numVisited < len(array)):
        # Multi-cycle check
        if (numVisited > 0 and currentIdx == STARTING_INDEX):
            return False
        currentIdx = getNextIdx(array, currentIdx)
    return currentIdx == STARTING_INDEX


def getNextIdx(array, idx):
    jumpValue = array[idx]
    # case when hops are greater than index
    nextIdx = (jumpValue + idx) % len(array)
    # case when hop value is negative
    if nextIdx >= 0:
        return nextIdx
    else:
        return nextIdx + len(array)
