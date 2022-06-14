class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, min_sum = -inf, inf 
        total = min_curr = max_curr = 0
        for num in nums:
            total += num
            
            max_curr += num
            if max_curr < num:
                max_curr = num
            max_sum = max(max_sum, max_curr)
            
            min_curr += num
            if min_curr > num:
                min_curr = num
            min_sum = min(min_sum, min_curr)
        return max(max_sum, total - min_sum) if max_sum > 0 else max_sum