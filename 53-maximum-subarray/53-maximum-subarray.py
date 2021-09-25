class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float('-inf')
        total = 0
        for num in nums:
            if total < 0 and total < num:
                total = 0
            total += num
            maximum = max(total, maximum)
        return maximum