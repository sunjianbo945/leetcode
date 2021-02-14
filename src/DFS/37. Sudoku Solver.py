from typing import *

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(board)

    def dfs(self, board):
        # test
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in range(1, 10):
                        if self.check_valid(board, i, j, str(k)):
                            board[i][j] = str(k)
                            if not self.dfs(board):
                                board[i][j] = '.'
                            else:
                                return True

                    if board[i][j] == '.':
                        return False

        return True

    def check_valid(self, board, x, y, number):

        for i in range(9):
            if board[x][i] == number or board[i][y] == number:
                return False

        left_row, left_column = x // 3, y // 3

        for i in range(3*left_row, 3*left_row + 3):
            for j in range(3*left_column, 3*left_column + 3):
                if board[i][j] == number:
                    return False

        return True

# Time Complexity - O(9m)， Space Complexity - O(m)
Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
)