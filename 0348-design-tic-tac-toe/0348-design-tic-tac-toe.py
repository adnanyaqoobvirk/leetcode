class TicTacToe:

    def __init__(self, n: int):
        self.b = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.b[row][col] = player

        rcount = ccount = mdcount = sdcount = 0
        for i in range(self.n):
            if self.b[row][i] == player:
                rcount += 1
            if self.b[i][col] == player:
                ccount += 1
            if self.b[i][i] == player:
                mdcount += 1
            if self.b[i][self.n - i - 1] == player:
                sdcount += 1
        
        return player if rcount == self.n or ccount == self.n or mdcount == self.n or sdcount == self.n else 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)