class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums) - 1
        dp = [False] * (n + 1)
        dp[n] = True
        for pos in range(n - 1, -1, -1):
            dp[pos] = any(dp[i] for i in range(min(pos + nums[pos], n), pos, -1))
        return dp[0]