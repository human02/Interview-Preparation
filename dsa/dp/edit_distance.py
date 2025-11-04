"""
Edit distance

Given two strings start and target, you need to determine the minimum number of operations required to convert the string
start into the string target. The operations you can use are:
-> Insert a character: Add any single character at any position in the string.
-> Delete a character: Remove any single character from the string.
-> Replace a character: Change any single character in the string to another character.

The goal is to transform start into target using the fewest number of these operations.

Examples:
Input: start = "planet", target = "plan"
Output: 2
Explanation:
To transform "planet" into "plan", the following operations are required:
1. Delete the character 'e': "planet" -> "plan"
2. Delete the character 't': "plan" -> "plan"
Thus, a total of 2 operations are needed.

Input: start = "abcdefg", target = "azced"
Output: 4
Explanation:
To transform "abcdefg" into "azced", the following operations are required:
1. Replace 'b' with 'z': "abcdefg" -> "azcdefg"
2. Delete 'd': "azcdefg" -> "azcefg"
3. Delete 'f': "azcefg" -> "azceg"
4. Replace 'g' with 'd': "azceg" -> "azced"
Thus, a total of 4 operations are needed.

Input: start = "saturday", target = "sunday"
Output: 3

Constraints:
1 ≤ start.length, target.length ≤ 1000
"""


class Solution:
    def editDistance_recur(self, start, target):
        m = len(start)
        n = len(target)
        return self.helper_recur(m - 1, n - 1, start, target)

    def helper_recur(self, i, j, s1, s2):
        # Base Case (either of the strs run out of indexes)
        if i < 0:
            return j + 1  # these many chars will be inserted
        if j < 0:
            return i + 1  # these many chars will be deleted
        # Same chars, hence nothing needs to be done
        if s1[i] == s2[j]:
            return 0 + self.helper_recur(i - 1, j - 1, s1, s2)
        else:
            return 1 + min(
                # insert
                self.helper_recur(i, j - 1, s1, s2),
                # delete
                self.helper_recur(i - 1, j, s1, s2),
                # replace
                self.helper_recur(i - 1, j - 1, s1, s2),
            )

    def editDistance_memo(self, start, target):
        m = len(start)
        n = len(target)

        # i,j are changing params. Both change from i-1 or j-1 to 0 which is n or m values
        dp = [[-1] * n for _ in range(m)]
        return self.helper_memo(m - 1, n - 1, start, target, dp)

    def helper_memo(self, i, j, s1, s2, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if dp[i][j] != -1:
            return dp[i][j]

        if s1[i] == s2[j]:
            dp[i][j] = 0 + self.helper_memo(i - 1, j - 1, s1, s2, dp)
            return dp[i][j]
        else:
            dp[i][j] = 1 + min(
                self.helper_memo(i, j - 1, s1, s2, dp),
                self.helper_memo(i - 1, j, s1, s2, dp),
                self.helper_memo(i - 1, j - 1, s1, s2, dp),
            )
            return dp[i][j]
