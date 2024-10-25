class NumArray:

    def __init__(self, nums: List[int]):
        def build(lo: int, hi: int, i: int) -> int:
            if lo == hi:
                self.s[i] = nums[lo]
            else:
                mid = lo + (hi - lo) // 2
                self.s[i] = build(lo, mid, i * 2 + 1) + build(mid + 1, hi, i * 2 + 2)
            return self.s[i]

        self.n = len(nums)
        self.s = [0] * 2**(ceil(log(self.n, 2)) + 1)
        build(0, self.n - 1, 0)

    def update(self, index: int, val: int) -> None:
        def update(lo: int, hi: int, i: int) -> None:
            if lo == hi:
                self.s[i] = val
            else:
                mid = lo + (hi - lo) // 2
                if index <= mid:
                    update(lo, mid, i * 2 + 1)
                else:
                    update(mid + 1, hi, i * 2 + 2)
                self.s[i] = self.s[i * 2 + 1] + self.s[i * 2 + 2]
        update(0, self.n - 1, 0)
                
    def sumRange(self, left: int, right: int) -> int:
        def query(lo: int, hi: int, i: int, l: int, r: int) -> int:
            if r < lo or l > hi:
                return 0
            elif l <= lo and r >= hi:
                return self.s[i]
            else:
                mid = lo + (hi - lo) // 2
                return query(lo, mid, i * 2 + 1, l, mid) + query(mid + 1, hi , i * 2 + 2, mid + 1, r)
        return query(0, self.n - 1, 0, left, right)
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)