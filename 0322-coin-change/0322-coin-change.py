class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = defaultdict(lambda: 10001)
        dp[0] = 0
        for m in range(min(coins), amount + 1):
            ans = 10001
            for c in coins:
                if m - c >= 0:
                    ans = min(ans, dp[m - c] + 1)
            dp[m] = ans
        return -1 if dp[amount] == 10001 else dp[amount]