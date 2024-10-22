class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = [0] + nums
        self.n = len(nums) + 1
        for i in range(1, self.n):
            p = i + (i & -i)
            if p < self.n:
                self.bit[p] += self.bit[i]

    def query(self, index: int) -> int:
        index += 1

        total = 0
        while index > 0:
            total += self.bit[index]
            index -= index & -index
        return total

    def update(self, index: int, val: int) -> None:
        d = val - self.nums[index]
        self.nums[index] = val
        index += 1
        while index < self.n:
            self.bit[index] += d
            index += index & -index

    def sumRange(self, left: int, right: int) -> int:
        return self.query(right) - self.query(left - 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)