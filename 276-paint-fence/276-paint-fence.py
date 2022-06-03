class Solution:
    def numWays(self, n: int, k: int) -> int:
        dp = [0] * (n + 2)
        dp[1] = k
        dp[2] = k * k
        for pos in range(3, n + 1):
            dp[pos] = (k - 1) * (dp[pos - 1] + dp[pos - 2])
        return dp[n]