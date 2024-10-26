class BIT2D:
    def __init__(self, matrix: List[List[int]]) -> None:
        self.m, self.n = len(matrix) + 1, len(matrix[0]) + 1
        self.matrix = [matrix[i][::] for i in range(self.m - 1)]
        self.tree = [[0] + (matrix[i - 1] if i > 0 else [0] * (self.n - 1)) for i in range(self.m)]
        for i in range(1, self.m):
            for j in range(1, self.n):
                p = j + (j & -j)
                if p < self.n:
                    self.tree[i][p] += self.tree[i][j]
        
        for j in range(1, self.n):
            for i in range(1, self.m):
                p = i + (i & -i)
                if p < self.m:
                    self.tree[p][j] += self.tree[i][j]
    
    def query(self, i: int, c: int) -> int:
        i += 1
        c += 1
        total = 0
        while i > 0:
            j = c
            while j > 0:
                total += self.tree[i][j]
                j -= j & -j
            i -= i & -i
        return total

    def update(self, i: int, c: int, v: int) -> None:
        d = v - self.matrix[i][c]
        self.matrix[i][c] = v
        i += 1
        c += 1
        while i < self.m:
            j = c
            while j < self.n:
                self.tree[i][j] += d
                j += j & -j
            i += i & -i
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.bit = BIT2D(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.bit.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.bit.query(row2, col2) - 
            self.bit.query(row1 - 1, col2) - 
            self.bit.query(row2, col1 - 1) + 
            self.bit.query(row1 - 1, col1 - 1)
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)