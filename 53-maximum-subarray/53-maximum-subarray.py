class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = total = float('-inf')
        for num in nums:
            total += num
            if total < num:
                total = num
            max_sum = max(max_sum, total)
        return max_sum