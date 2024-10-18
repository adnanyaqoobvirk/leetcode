class TicTacToe:

    def __init__(self, n: int):
        self.counts = [[0] * n for _ in range(2)]
        self.mdcount = self.sdcount = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        sign = -1 if player == 1 else 1
        self.counts[0][row] += sign
        self.counts[1][col] += sign
        if row - col == 0:
            self.mdcount += sign
        if row + col == self.n - 1:
            self.sdcount += sign

        return player if sign * self.n in (
            self.counts[0][row],
            self.counts[1][col],
            self.mdcount,
            self.sdcount
        ) else 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)