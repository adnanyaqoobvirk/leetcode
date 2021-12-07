class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest_sum, total = float('-inf'), 0
        for num in nums:
            total += num
            if total < num:
                total = num
            largest_sum = max(largest_sum, total)
        return largest_sum