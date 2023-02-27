class NumArray:

    def __init__(self, nums: List[int]):
        prefix = 0
        self.prefix = []
        for num in nums:
            prefix += num
            self.prefix.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        prev = 0 if left == 0 else self.prefix[left - 1]
        return self.prefix[right] - prev

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)