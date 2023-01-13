"""

Write a Min Max Stack class for a Min Max Stack. The class should support:

- Pushing and popping values on and off the stack.
- Peeking at the value at the top of the stack.
- Getting both the minimum and the maximum values in the stack at any given point in time.
  

  All class methods, when considered independently, should run in constant time
  and with constant space.

  Sample Usage:

  // All operations below are performed sequentially.
  MinMaxStack(): -
  push(5): -
  getMin(): 5
  getMax(): 5
  peek(): 5
  push(7): -
  getMin(): 5
  getMax(): 7
  peek(): 7
  push(2): -
  getMin(): 2
  getMax(): 7
  peek(): 2
  pop(): 2
  pop(): 7
  getMin(): 5
  getMax(): 5
  peek(): 5

"""
# Feel free to add new properties and methods to the class.


class MinMaxStack:

    def __init__(self):
        # creating a min-max stack to have min and max vaue at every step
        self.minMaxStack = []
    # normal stack for push etc
        self.stack = []

    def peek(self):
        return self.stack[len(self.stack)-1]
       # this also works -> return self.stack[-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        # for first element push min and max will be same at that step.
        nextMinMax = {"min": number, "max": number}
        if (len(self.stack)):
            nextMinMax["min"] = min(self.minMaxStack[-1]["min"], number)
            nextMinMax["max"] = max(self.minMaxStack[-1]["max"], number)
        self.minMaxStack.append(nextMinMax)
        self.stack.append(number)
        # return number

    def getMin(self):
        return self.minMaxStack[-1]["min"]

    def getMax(self):
        return self.minMaxStack[-1]["max"]
