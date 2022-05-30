class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for r in range(coin, amount + 1):
                dp[r] = min(
                    dp[r],
                    dp[r - coin] + 1
                )
        return -1 if dp[amount] == float('inf') else dp[amount]