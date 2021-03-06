class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for m in range(2, n + 1):
            for i in range(1, m + 1):
                dp[m] += dp[i - 1] * dp[m - i]
        return dp[n]