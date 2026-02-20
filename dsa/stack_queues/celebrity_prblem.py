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


class Solution:
    # TC - O(n^2), SC - O(n)
    def celebrity_brute(self, M):
        """
        Idea:
        - Keep 2 lists iKnow,knowMe
        - iterate through each element and update the lists
        - index with (n-1) - knowMe and 0 - iKnow is the celebrity
        """

        # Size of given matrix
        n = len(M)

        # To store count of people who know person of index i
        knowMe = [0] * n

        # To store count of people who the person of index i knows
        iKnow = [0] * n

        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    knowMe[j] += 1
                    iKnow[i] += 1

        for i in range(n):
            if knowMe[i] == n - 1 and iKnow[i] == 0:
                return i

        # Return -1 if no celebrity is found
        return -1
if __name__ == "__main__":
    obj = Solution()

    print(obj.celebrity_brute([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]))
    print(obj.celebrity_brute([[0, 1], [1, 0]]))
