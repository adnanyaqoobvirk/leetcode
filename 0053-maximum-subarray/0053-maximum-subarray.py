class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, total = -inf, 0
        for num in nums:
            total = max(total + num, num)
            ans = max(ans, total)
        return ans