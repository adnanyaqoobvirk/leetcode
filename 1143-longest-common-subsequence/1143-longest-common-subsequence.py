class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                dp[i][j] = (
                    (1 + dp[i - 1][j - 1]) 
                    if text1[i] == text2[j]
                    else max(dp[i][j - 1], dp[i - 1][j])
                )
        return dp[n - 1][m - 1]