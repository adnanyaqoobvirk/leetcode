class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        total = 0
        for num in nums:
            total += num
            if total < num:
                total = num
            maximum = max(total, maximum)
        return maximum