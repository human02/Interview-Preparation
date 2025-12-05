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
    # TC - Exponential, SC - O(m+n)
    def editDistance_recur(self, start, target):
        m = len(start)
        n = len(target)

        def helper_recur(i, j):
            # Base Case (either of the strs run out of indexes)
            if i < 0:
                return j + 1  # these many chars will be inserted
            if j < 0:
                return i + 1  # these many chars will be deleted

            # Same chars, hence nothing needs to be done
            if start[i] == target[j]:
                return 0 + helper_recur(i - 1, j - 1)
            # not same chars, so either of 3 operations will take place.
            else:
                return 1 + min(
                    # insert
                    helper_recur(i, j - 1),
                    # delete
                    helper_recur(i - 1, j),
                    # replace
                    helper_recur(i - 1, j - 1),
                )

        return helper_recur(m - 1, n - 1)

    # TC - O(m*n), SC - O(m+n) for stack space + O(m*n) for array space
    def editDistance_memo(self, start, target):
        m = len(start)
        n = len(target)

        # i,j are changing params. Both change from i-1 or j-1 to 0 which is n or m values
        dp = [[-1] * n for _ in range(m)]

        def helper_memo(i, j, dp):
            if i < 0:
                return j + 1
            if j < 0:
                return i + 1

            if dp[i][j] != -1:
                return dp[i][j]

            if start[i] == target[j]:
                dp[i][j] = 0 + helper_memo(i - 1, j - 1, dp)
                return dp[i][j]
            else:
                dp[i][j] = 1 + min(
                    helper_memo(i, j - 1, dp),
                    helper_memo(i - 1, j, dp),
                    helper_memo(i - 1, j - 1, dp),
                )
                return dp[i][j]

        return helper_memo(m - 1, n - 1, dp)


if __name__ == "__main__":
    obj = Solution()
    print(f"\nRecursive Solution:\n{obj.editDistance_recur("planet","plan")}")
    print(f"{obj.editDistance_recur("abcdefg","azced")}")
    print(f"{obj.editDistance_recur("saturday","sunday")}")
    print(f"\nMemoized Solution:\n{obj.editDistance_memo("planet","plan")}")
    print(f"{obj.editDistance_memo("abcdefg","azced")}")
    print(f"{obj.editDistance_memo("saturday","sunday")}\n")
