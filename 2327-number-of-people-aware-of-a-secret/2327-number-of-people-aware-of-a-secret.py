class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * n
        dp[0] = 1
        for i in range(n):
            for j in range(min(n, i + delay), min(n, i + forget)):
                dp[j] += dp[i]
            dp[i] %= MOD
        return sum(dp[i] for i in range(n - forget, n)) % MOD