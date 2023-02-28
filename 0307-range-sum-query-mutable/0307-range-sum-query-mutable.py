class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.t = [0] * self.n + arr
        for i in range(len(arr) - 1, 0, -1):
            self.t[i] = self.t[i << 1] + self.t[i << 1 | 1]
    
    def update(self, i, v):
        i += self.n
        self.t[i] = v
        while i > 1:
            self.t[i >> 1] = self.t[i] + self.t[i ^ 1]
            i >>= 1
            
    def query(self, i, j):
        i += self.n
        j += self.n
        ans = 0
        while i <= j:
            if i & 1:
                ans += self.t[i]
                i += 1
            i >>= 1
            if not (j & 1):
                ans += self.t[j]
                j -= 1
            j >>= 1
        return ans
    
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