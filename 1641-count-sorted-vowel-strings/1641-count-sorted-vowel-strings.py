class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * 6 for _ in range(n + 1)]
        dp[n] = [1] * 6
        for i in reversed(range(5)):
            for j in reversed(range(n)):
                dp[j][i] = dp[j][i + 1] + dp[j + 1][i]
        return dp[0][0]