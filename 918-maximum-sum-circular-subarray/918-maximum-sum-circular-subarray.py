class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum, curr = -inf, 0
        for num in nums:
            curr += num
            if curr < num:
                curr = num
            max_sum = max(max_sum, curr)
        
        min_sum, curr = inf, 0
        for num in nums:
            curr += num
            if curr > num:
                curr = num
            min_sum = min(min_sum, curr)
        
        ans = max(max_sum, sum(nums) - min_sum)
        return ans if ans != 0 else max_sum