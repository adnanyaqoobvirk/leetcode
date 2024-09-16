class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.psums = [matrix[i][::] for i in range(self.m)]
        for i in reversed(range(self.m)):
            for j in reversed(range(self.n)):
                if i + 1 < self.m:
                    self.psums[i][j] += self.psums[i + 1][j]
                
                if j + 1 < self.n:
                    self.psums[i][j] += self.psums[i][j + 1]

                if i + 1 < self.m and j + 1 < self.n:
                    self.psums[i][j] -= self.psums[i + 1][j + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.psums[row1][col1]
        if col2 + 1 < self.n:
            ans -= self.psums[row1][col2 + 1]
        
        if row2 + 1 < self.m:
            ans -= self.psums[row2 + 1][col1]
        
        if col2 + 1 < self.n and row2 + 1 < self.m:
            ans += self.psums[row2 + 1][col2 + 1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)