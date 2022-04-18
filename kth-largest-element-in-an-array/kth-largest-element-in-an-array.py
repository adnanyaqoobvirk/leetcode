class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        heapify(nums)
        
        for _ in range(1, k):
            heappop(nums)
        return -heappop(nums)