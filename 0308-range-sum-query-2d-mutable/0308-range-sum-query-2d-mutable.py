class SegTree:
    def __init__(self, nums: List[int]) -> None:
        self.n = len(nums)
        self.stree = [0] * self.n + nums
        for i in reversed(range(self.n)):
            self.stree[i] = self.stree[i << 1] + self.stree[i << 1 | 1]

    def query(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n + 1
        total = 0
        while l < r:
            if l & 1:
                total += self.stree[l]
                l += 1
            if r & 1:
                r -= 1
                total += self.stree[r]
            l >>= 1
            r >>= 1
        return total

    def update(self, idx: int, val: int) -> None:
        i = idx + self.n
        self.stree[i] = val
        i >>= 1
        while i > 0:
            self.stree[i] = self.stree[i << 1] + self.stree[i << 1 | 1]
            i >>= 1

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.trees = [SegTree(row) for row in matrix]

    def update(self, row: int, col: int, val: int) -> None:
        self.trees[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.trees[r].query(col1, col2)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)