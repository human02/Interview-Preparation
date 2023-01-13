"""

  Write a function that takes in a string made up of brackets ( (,[,{,),],} )
  and other optional characters. The function should return a boolean representing 
  whether the string is balanced with regards to brackets.

  A string is said to be balanced if it has as many opening brackets of a
  certain type as it has closing brackets of that type and if no bracket is
  unmatched. Note that an opening bracket can't match a corresponding closing
  bracket that comes before it, and similarly, a closing bracket can't match a
  corresponding opening bracket that comes after it. Also, brackets can't
  overlap each other as in [(])

  Input:
    string = "([])(){}(())()()"

  Output:
    true
  
"""

# O(n) - time | O(n) - space
# space complexity reason - when only open brackets in the string.


def balancedBrackets(string):
    stack = []
    openBrackets = "({["
    closedBrackets = ")}]"
    check = {')': '(', ']': '[', '}': '{'}
    for char in string:
        if (char in openBrackets):
            stack.append(char)
        elif char in closedBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == check[char]:
                stack.pop()
            # case when more closed brackets in the input
            else:
                return False

    return len(stack) == 0
