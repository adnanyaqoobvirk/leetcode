class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        b_count = 0
        for i in range(1, len(s) + 1):
            if s[i - 1] == 'a':
                dp[i] = min(dp[i - 1] + 1, b_count)
            else:
                dp[i] = dp[i - 1]
                b_count += 1
        return dp[len(s)]