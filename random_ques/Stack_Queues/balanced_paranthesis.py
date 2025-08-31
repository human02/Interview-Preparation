"""
Balanced Paranthesis

Given string str containing just the characters '(', ')', '{', '}', '[' and ']', check if the input string is valid 
and return true if the string is balanced otherwise return false.

Example 1:
Input: str = “()[{}()]”

Output: True
Explanation: As every open bracket has its corresponding close bracket. Match parentheses are in correct order 
hence they are balanced.

Example 2:
Input: str = “[()”
Output: False
Explanation: As ‘[‘ does not have ‘]’ hence it is not valid and will return false.

Example 3:
Input: str = "{[()]}"
Output:True

Constraints:
- 1 <= str.length <= 104
- str consists of parentheses only '()[]{}'.
"""

class Solution:
    def helper(self,closed,st_top):
        if((closed==')' and st_top=='(') or (closed=='}' and st_top=='{') or (closed==']' and st_top=='[')):
            return True
        return False

    def isValid(self, str: str) -> bool:
        st=[]
        for i in str:
            if (i == '('or i=='{' or i =='['):
                st.append(i)
            else:
                if not st:
                    return False
                ch = st[-1]
                st.pop()
                if not self.helper(i, ch):
                    return False
        return not st
    
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ("()[{}()]", True),
        ("[()", False),
        ("{[()]}", True)
    ]
    for s, expected in test_cases:
        result = sol.isValid(s)
        print(f"\nInput: {s}\nOutput: {result}\nExpected: {expected}\n")
        
