class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = -inf 
        total = 0
        for num in nums:
            total += num
            if total < num:
                total = num
            ans = max(ans, total)
        return ans