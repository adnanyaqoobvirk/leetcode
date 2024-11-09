class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        n = len(s) + 1
        dp = [[0] * n for _ in range(n)]
        ans = 0
        for i in reversed(range(n - 1)):
            for j in reversed(range(i)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                    ans = max(ans, dp[i][j])
        return ans
