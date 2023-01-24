"""


"""
# Idea: To traverse the array from left (twice) and check if stack has either any index value and
# currentIdx value > stack top index value
# Then pop the index from stack and put currentIdx value to the result array and keep doing it.


# O(n) time | O(n) space
def nextGreaterElement(array):
    # initiatise result list to store
    result = [-1] * len(array)
    stack = []

    # Circular constraint in the array needs twice traversal
    for idx in range(2 * len(array)):
        # getting to the back indexes
        circularIdx = idx % len(array)
        # if value @ circularIdx > value @ top of stack index
        while len(stack) > 0 and array[circularIdx] > array[stack[len(stack) - 1]]:
            # add larger value to stack value index in result list
            top = stack.pop()
            result[top] = array[circularIdx]
        # if value @circularIdx < value @ top of stack index
        stack.append(circularIdx)
    return result
