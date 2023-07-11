class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-inf] * 2 for _ in range(n + 1)]
        dp[0][1] = 0
        
        for i in range(1, n + 1):
            dp[i][1] = max(0, nums[i - 1] + dp[i - 1][1])
            dp[i][0] = max(nums[i - 1] + dp[i - 1][1], dp[i - 1][0])
        return dp[n][0]