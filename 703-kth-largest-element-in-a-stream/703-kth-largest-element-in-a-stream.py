class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        self.nums, self.k = nums, k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k :
            heappush(self.nums, val)
        elif self.nums[0] <= val:
            heappushpop(self.nums, val)
        return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)