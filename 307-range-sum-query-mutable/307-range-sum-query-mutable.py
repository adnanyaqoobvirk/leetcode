class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tree = [0] * (4 * len(nums))
        
        self.buildTree(0, 0, len(nums) - 1)
        
    def update(self, index: int, val: int) -> None:
        self.updateTree(0, index, 0, len(self.nums) - 1, val)

    def sumRange(self, left: int, right: int) -> int:
        return self.searchTree(0, 0, len(self.nums) - 1, left, right)

    def updateTree(self, curr: int, index: int, lo: int, hi: int, val: int) -> None:
        if lo == hi:
            self.tree[curr] = val
            return
        
        mid = lo + (hi - lo) // 2
        
        if index <= mid:
            self.updateTree(2 * curr + 1, index, lo, mid, val)
        elif index > mid:
            self.updateTree(2 * curr + 2, index, mid + 1, hi, val)
            
        self.tree[curr] = self.tree[2 * curr + 1] + self.tree[2 * curr + 2]
        
    def searchTree(self, curr: int, lo: int, hi: int, left: int, right: int) -> int:
        if hi < lo or lo > right:
            return 0
        
        if left <= lo and right >= hi:
            return self.tree[curr]
        
        mid = lo + (hi - lo) // 2
        
        if right <= mid:
            return self.searchTree(2 * curr + 1, lo, mid, left, right)
        elif left > mid:
            return self.searchTree(2 * curr + 2, mid + 1, hi, left, right)
        else:
            l = self.searchTree(2 * curr + 1, lo, mid, left, right)
            r = self.searchTree(2 * curr + 2, mid + 1, hi, left, right)
            
            return l + r
        
    def buildTree(self, curr: int, lo: int, hi: int) -> None:
        if lo == hi:
            self.tree[curr] = self.nums[lo]
            return
        
        mid = lo + (hi - lo) // 2

        self.buildTree(2 * curr + 1, lo, mid)
        self.buildTree(2 * curr + 2, mid + 1, hi)

        self.tree[curr] = self.tree[2 * curr + 1] + self.tree[2 * curr + 2]
            
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)