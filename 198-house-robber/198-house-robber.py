class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i] = max(
                nums[i] + dp[i - 2],
                dp[i - 1]
            )
        return dp[n - 1]