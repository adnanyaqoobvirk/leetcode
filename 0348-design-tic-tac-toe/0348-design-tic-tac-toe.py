class TicTacToe:

    def __init__(self, n: int):
        self.p1counts = [[0] * n for _ in range(2)]
        self.p1mdcounts = 0
        self.p1sdcounts = 0
        self.p2counts = [[0] * n for _ in range(2)]
        self.p2mdcounts = 0
        self.p2sdcounts = 0
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.p1counts[0][row] += 1
            self.p1counts[1][col] += 1
            if row - col == 0:
                self.p1mdcounts += 1
            if row + col == self.n - 1:
                self.p1sdcounts += 1

            return 1 if (
                self.p1counts[0][row] == self.n or
                self.p1counts[1][col] == self.n or
                self.p1mdcounts == self.n or
                self.p1sdcounts == self.n
            ) else 0
        else:
            self.p2counts[0][row] += 1
            self.p2counts[1][col] += 1
            if row - col == 0:
                self.p2mdcounts += 1
            if row + col == self.n - 1:
                self.p2sdcounts += 1
            
            return 2 if (
                self.p2counts[0][row] == self.n or
                self.p2counts[1][col] == self.n or
                self.p2mdcounts == self.n or
                self.p2sdcounts == self.n
            ) else 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)