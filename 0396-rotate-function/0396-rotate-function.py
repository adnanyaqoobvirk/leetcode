class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        total = 0
        for i, num in enumerate(nums):
            f += i * num
            total += num
        
        n = len(nums)
        max_f = f
        for i in reversed(range(1, n)):
            f = f - (n - 1) * nums[i] + total - nums[i]
            max_f = max(max_f, f)
        
        return max_f