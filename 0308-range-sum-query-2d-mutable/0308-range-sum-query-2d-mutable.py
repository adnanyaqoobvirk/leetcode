class BIT:
    def __init__(self,  nums: List[int]) -> None:
        self.nums = nums
        self.n = len(nums) + 1
        self.tree = [0] + nums
        for i in range(1, self.n):
            p = i + (i & -i)
            if p < self.n:
                self.tree[p] += self.tree[i]
    
    def query(self, i: int) -> int:
        i += 1
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def update(self, i: int, v: int) -> None:
        d = v - self.nums[i]
        self.nums[i] = v
        i += 1
        while i < self.n:
            self.tree[i] += d
            i += i & -i
        
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m, self.n = len(matrix), len(matrix[0])
        self.bits = [BIT(row) for row in matrix]

    def update(self, row: int, col: int, val: int) -> None:
        self.bits[row].update(col, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for r in range(row1, row2 + 1):
            total += self.bits[r].query(col2) - self.bits[r].query(col1 - 1)
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)