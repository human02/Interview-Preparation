"""
Word Search

Given a grid of n x m dimension grid of characters board and a string word.
The word can be created by assembling the letters of successively surrounding cells,
whether they are next to each other vertically or horizontally.
It is forbidden to use the same letter cell more than once.

Return true if the word exists in the grid otherwise false.

Example 1:
board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , word = "ABCCED"
Output: true

Example 2:
board = [ ["A", "B", "C", "E"] , ["S" ,"F" ,"C" ,"S"] , ["A", "D", "E", "E"] ] , word = "SEE"
Output: true
"""


class Solution:
    def exist(self, board, word):
        # your code goes here
        rows = len(board)
        cols = len(board[0])

        def helper(i, j, w_idx):
            # Base Cases
            if w_idx == len(word):
                return True
            if i < 0 or j < 0 or i >= rows or j >= cols or word[w_idx] != board[i][j]:
                return False

            # Back Tracking Mechanism
            tmp = board[i][j]
            board[i][j] = "#"
            res = (
                helper(i + 1, j, w_idx + 1)
                or helper(i, j + 1, w_idx + 1)
                or helper(i - 1, j, w_idx + 1)
                or helper(i, j - 1, w_idx + 1)
            )
            board[i][j] = tmp
            return res

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    if helper(i, j, 0):
                        return True
        return False
