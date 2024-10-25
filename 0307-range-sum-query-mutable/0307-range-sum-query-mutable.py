class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n
        self.tree[i] = val
        
        p = i >> 1
        while p > 0:
            self.tree[p] = self.tree[p << 1] + self.tree[p << 1 | 1]
            p >>= 1

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        l, r = left + self.n, right + self.n + 1
        while l < r:
            if l & 1:
                total += self.tree[l]
                l += 1
            l >>= 1
            if r & 1:
                r -= 1
                total += self.tree[r]
            r >>= 1
        return total


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)