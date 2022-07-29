class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (len(nums) + 1)
        for i, num in enumerate(nums):
            self.updateTree(i, num)
        
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.updateTree(index, diff)

    def sumRange(self, left: int, right: int) -> int:
        return self.getSum(right) - self.getSum(left - 1)

    def getSum(self, index) -> int:
        ans = 0
        index += 1
        while index > 0:
            ans += self.tree[index]
            index -= index & -index
        return ans
    
    def updateTree(self, index: int, val: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += val
            index += index & -index
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)