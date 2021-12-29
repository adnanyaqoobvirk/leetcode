class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        h = [nums[i] for i in range(min(len(nums), 3))]
        heapify(h)
        for i in range(3, len(nums)):
            if h[0] < nums[i]:
                heappushpop(h, nums[i])
        return h[0] if len(h) >= 3 else max(h)