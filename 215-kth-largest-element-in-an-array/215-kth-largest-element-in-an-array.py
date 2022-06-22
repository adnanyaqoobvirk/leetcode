class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        larger = k < n // 2
        
        if larger:
            nums = [-num for num in nums]
            
        heapify(nums)
        for _ in range(k - 1 if larger else n - k):
            heappop(nums)
        return -heappop(nums) if larger else heappop(nums)