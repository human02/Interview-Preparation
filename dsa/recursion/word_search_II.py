"""

Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells
are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
       words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:
    m == board.length
    n == board[i].length
    1 <= m, n <= 12
    board[i][j] is a lowercase English letter.
    1 <= words.length <= 3 * 104
    1 <= words[i].length <= 10
    words[i] consists of lowercase English letters.
    All the strings of words are unique.

"""


class Solution:
    def findWords(self, board, word):
        """
        Idea:
        - We traverse through all indexes and start recursive check if word[0] == grid[i][j].
        -
        """
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
