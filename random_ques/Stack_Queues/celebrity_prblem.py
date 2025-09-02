"""
Celebrity Problem

A celebrity is a person who is known by everyone else at the party but does not know anyone in return. 
Given a square matrix M of size N x N where M[i][j] is 1 if person i knows person j, and 0 otherwise, 
determine if there is a celebrity at the party. Return the index of the celebrity or -1 if no such person exists.
Note that M[i][i] is always 0.


Input: M = [ [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0] ]
Output: 1
Explanation: Person 1 does not know anyone and is known by persons 0, 2, and 3. Therefore, person 1 is the celebrity.

Input: M = [ [0, 1], [1, 0] ]
Output: -1
Explanation: Both persons know each other, so there is no celebrity.
"""

# Brute, search every row and column, O(N^2),
# create 2 list to track who knows whom and who is known by whom.
# class Solution:
#     # Function to find the index of celebrity
#     def celebrity(self, M):
        
#         # Size of given matrix
#         n = len(M)
        
#         # To store count of people who 
#         # know person of index i
#         knowMe = [0] * n
        
#         # To store count of people who 
#         # the person of index i knows
#         Iknow = [0] * n
        
#         # Traverse on given matrix
#         for i in range(n):
#             for j in range(n):
                
#                 # If person i knows person j
#                 if M[i][j] == 1:
#                     knowMe[j] += 1
#                     Iknow[i] += 1
        
#         # Traverse for all persons to find the celebrity
#         for i in range(n):
            
#             # Return the index of celebrity
#             if knowMe[i] == n - 1 and Iknow[i] == 0:
#                 return i  
        
#         # Return -1 if no celebrity is found
#         return -1

# Optimal, two pointer approach, O(N)
# who knows who, if A knows B, A cannot be celebrity, if A does not know B, B cannot be celebrity.
# So we can eliminate one person in each comparison.
class Solution:
    # Function to find the index of celebrity
    def celebrity(self, M):
        
        # Size of given matrix
        n = len(M)
        
        # Top and Down pointers
        top, down = 0, n - 1
        
        # Traverse for all the people
        while top < down:
            
            # If top knows down,
            # it can not be a celebrity
            if M[top][down] == 1:
                top += 1
            
            # If down knows top,
            # it can not be a celebrity
            elif M[down][top] == 1:
                down -= 1
            
            # If both do not know each other,
            # both cannot be the celebrity
            else:
                top += 1
                down -= 1
        
        # Return -1 if no celebrity is found
        if top > down:
            return -1
        
        # Check if the person pointed by top is celebrity (row and column check in matrix)
        for i in range(n):
            if i == top:
                continue
            
            # Check if it is not a celebrity
            if M[top][i] == 1 or M[i][top] == 0:
                return -1
        
        # Return the index of celebrity
        return top

if __name__ == "__main__":
    M = [
        [0, 1, 1, 0], 
        [0, 0, 0, 0], 
        [1, 1, 0, 0], 
        [0, 1, 1, 0]
    ]
    
    # Creating an instance of 
    # Solution class
    sol = Solution() 
    
    # Function call to find the index of celebrity
    ans = sol.celebrity(M)
    
    print("The index of celebrity is:", ans)

