class FenwickTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr) + 1
        self.t = [0] + arr
        for i in range(1, self.n):
            p = i + (i & -i)
            if p < self.n:
                self.t[p] += self.t[i]
        
    def update(self, i, v):
        d = v - self.arr[i]
        self.arr[i] = v
        i += 1
        while i < self.n:
            self.t[i] += d
            i += i & -i
        
    def query(self, i):
        i += 1
        ans = 0
        while i > 0:
            ans += self.t[i]
            i -= i & -i
        return ans
    
class NumArray:

    def __init__(self, nums: List[int]):
        self.t = FenwickTree(nums)

    def update(self, index: int, val: int) -> None:
        self.t.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.t.query(right)
        else:
            return self.t.query(right) - self.t.query(left - 1)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)