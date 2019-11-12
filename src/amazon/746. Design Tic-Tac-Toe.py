
class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.adiag = 0
        self.mp = {1:1, 2:-1}
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.rows[row]+=self.mp[player]
        self.cols[col]+=self.mp[player]
        
        targets = [self.rows[row], self.cols[col]]

        if row==col:
            self.diag+=self.mp[player]
            targets.append(self.diag)

        if row+col==self.n-1:
            self.adiag+=self.mp[player]
            targets.append(self.adiag)

        for target in targets:
            if target == self.n: return 1
            if target == 0-self.n: return 2
        return 0