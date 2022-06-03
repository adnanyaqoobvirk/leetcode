class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for pos in range(n):
            dp[pos][0] = 1
            
        for pos in reversed(range(n)):
            for remaining in range(1, amount + 1):
                dp[pos][remaining] = (
                    ((dp[pos][remaining - coins[pos]]) if remaining >= coins[pos] else 0)
                    + dp[pos + 1][remaining]
                )
        return dp[0][amount]