from typing import *


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for i in range(n)]
        res = []
        self.dfs(board, 0, res, set())
        return res

    def dfs(self, board, row, res, visited):

        if row >= len(board):
            res.append([''.join(board[i]) for i in range(len(board))])
            return

        for col in range(len(board)):

            if col not in visited and self.check_dig(board, row, col):
                board[row][col] = 'Q'
                visited.add(col)
                self.dfs(board, row + 1, res, visited)
                visited.remove(col)
                board[row][col] = '.'

    def check_dig(self, board, x, y):

        # check left top
        i, left_j, right_j = x, y, y
        while i >= 0:
            if left_j >= 0 and board[i][left_j] == 'Q':
                return False
            if right_j < len(board) and board[i][right_j] == 'Q':
                return False
            i -= 1
            left_j -= 1
            right_j += 1

        return True


Solution().solveNQueens(4)