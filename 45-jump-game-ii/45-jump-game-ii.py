class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf') for _ in range(n + 1)]
        dp[n - 1] = 0
        for i in reversed(range(n)):
            for j in range(i + 1, min(n, i + nums[i] + 1)):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]