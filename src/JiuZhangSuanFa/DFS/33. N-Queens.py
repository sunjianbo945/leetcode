class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """

    def solveNQueens(self, n):
        # write your code here
        board = [['.' for i in range(n)] for i in range(n)]
        loc = [i for i in range(n)]
        res = []
        self.recur(board, 0, loc, res)
        return res

    def recur(self, board, row, loc, res):

        if not loc:
            res.append([''.join(board[i]) for i in range(len(board))])
            return

        for i in range(len(loc)):

            if self.is_valid(board, row, loc[i]):
                board[row][loc[i]] = 'Q'
                self.recur(board, row + 1, loc[:i] + loc[i + 1:], res)
                board[row][loc[i]] = '.'

    def is_valid(self, grid, row, column):

        x, y = row, column
        if not self.right_down(grid, x, y) or not self.right_up(grid, x, y) or not self.left_up(grid, x,
                                                                                                y) or not self.left_down(
                grid, x, y):
            return False

        return True

    def right_down(self, grid, x, y):

        while x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):

            if grid[x][y] == 'Q':
                return False

            x += 1
            y += 1

        return True

    def right_up(self, grid, x, y):

        while x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):

            if grid[x][y] == 'Q':
                return False

            x -= 1
            y += 1

        return True

    def left_up(self, grid, x, y):

        while x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):

            if grid[x][y] == 'Q':
                return False

            x -= 1
            y -= 1

        return True

    def left_down(self, grid, x, y):

        while x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]):

            if grid[x][y] == 'Q':
                return False

            x += 1
            y -= 1

        return True