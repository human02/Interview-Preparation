"""

  You're given an array of integers where each integer represents a jump of its
  value in the array. For instance, the integer 2  represents a jump
  of two indices forward in the array; the integer -3 represents a
  jump of three indices backward in the array.

  If a jump spills past the array's bounds, it wraps over to the other side. For
  instance, a jump of -1 at index 0 brings us to the last index in the array. 
  Similarly, a jump of 1 at the last index in the array brings us to index 0.

  Write a function that returns a boolean representing whether the jumps in the
  array form a single cycle. A single cycle occurs if, starting at any index in
  the array and following the jumps, every element in the array is visited
  exactly once before landing back on the starting index.

  Sample Input:
    array = [2, 3, 1, -4, -4, 2]

  Sample Output:
    true

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
