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

    # TC - O(n), SC - O(1)
    def celebrity_optimal(self, M):
        """
        Idea:
        - We use elimination method in finding who is not the celebrity.
        - Min 0 celebrity or at max there can be 1 celebrity
        - We have 2 pointer, top and down and we compare these values (pair wise)
            - we check if either of the two know each other
                - we eliminate the one that knows and update that pointer
                    - +1 for top or -1 for down
                - in the end top and down will reach 1 element
            - if both dont know each other or know each other then both are not celebrity
                - as celebrity needs to be known by all
                - top doesnt know down
                - down doesnt know top
                - hence eliminate both
            - we then check this complete row to confirm if this person is celebrity
        """
        n = len(M)

        top, down = 0, n - 1

        while top < down:
            if M[top][down] == 1:
                top += 1

            elif M[down][top] == 1:
                down -= 1

            else:
                top += 1
                down -= 1

        # Return -1 if no celebrity is found - important check
        if top > down:
            return -1

        # Checking top(remaning)
        for i in range(n):
            if i == top:  # skip checking itself
                continue

            # Check if it is not a celebrity
            if M[top][i] == 1 or M[i][top] == 0:
                return -1

        return top


if __name__ == "__main__":
    obj = Solution()

    print(obj.celebrity_brute([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]))
    print(obj.celebrity_brute([[0, 1], [1, 0]]))
    print(
        obj.celebrity_optimal([[0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]])
    )
    print(obj.celebrity_optimal([[0, 1], [1, 0]]))
