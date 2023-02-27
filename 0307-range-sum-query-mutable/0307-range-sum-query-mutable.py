class SegmentTree:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.t = [0] * (2 ** (ceil(log2(self.n)) + 1))
        
        self._build(1, 0, self.n - 1)
    
    def _build(self, ti, l, r):
        if l == r:
            self.t[ti] = self.arr[l]
        else:
            m = (l + r) >> 1
            self.t[ti] = self._build(ti << 1, l, m) + self._build(ti << 1 | 1, m + 1, r)
        return self.t[ti]
    
    def _update(self, v, i, ti, l, r):
        if l == r:
            self.t[ti] = v
        else:
            m = (l + r) >> 1
            if i <= m:
                self._update(v, i, ti << 1, l, m)
            else:
                self._update(v, i, ti << 1 | 1, m + 1, r)
            self.t[ti] = self.t[ti << 1] + self.t[ti << 1 | 1]
    
    def _query(self, ti, i, j, l, r):
        if l > j or r < i:
            return 0
        
        if l >= i and r <= j:
            return self.t[ti]
    
        m = (l + r) >> 1
        return self._query(ti << 1, i, j, l, m) + self._query(ti << 1 | 1, i, j, m + 1, r)
    
    def update(self, i, v):
        self._update(v, i, 1, 0, self.n - 1)
        
    def query(self, i, j):
        return self._query(1, i, j, 0, self.n - 1)
        
class NumArray:

    def __init__(self, nums: List[int]):
        self.t = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.t.update(index, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.t.query(left, right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)