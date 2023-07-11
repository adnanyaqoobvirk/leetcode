class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        p1, p2 = -inf, 0
        for i in range(len(nums)):
            p1, p2 = max(nums[i] + p2, p1), max(0, nums[i] + p2)
        return p1