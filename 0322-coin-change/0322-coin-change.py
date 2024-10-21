class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [inf] * (amount + 1)
        dp[0] = 0
        for m in range(1, amount + 1):
            ans = inf
            for c in coins:
                if m - c >= 0:
                    ans = min(ans, dp[m - c] + 1)
            dp[m] = ans
        return -1 if dp[amount] == inf else dp[amount]