class SegTree2D:
    def __init__(self, matrix):
        self.m, self.n = len(matrix), len(matrix[0])
        self.t = [[0] * (2 * self.n) for _ in range(2 * self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])
    
    def update(self, r, c, v):
        r += self.m
        c += self.n

        d = v - self.t[r][c]
        while r > 0:
            j = c
            while j > 0:
                self.t[r][j] += d
                j >>= 1
            r >>= 1

    def _query(self, i, l, r):
        l += self.n
        r += self.n + 1
        ans = 0
        while l < r:
            if l & 1:
                ans += self.t[i][l]
                l += 1
            if r & 1:
                r -= 1
                ans += self.t[i][r]
            l >>= 1
            r >>= 1
        return ans

    def query(self, r1, c1, r2, c2):
        i = r1 + self.m
        j = r2 + self.m + 1
        ans = 0
        while i < j:
            if i & 1:
                ans += self._query(i, c1, c2)
                i += 1
            if j & 1:
                j -= 1
                ans += self._query(j, c1, c2)
            i >>= 1
            j >>= 1
        return ans

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.t = SegTree2D(matrix)

    def update(self, row: int, col: int, val: int) -> None:
        self.t.update(row, col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.t.query(row1, col1, row2, col2)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)