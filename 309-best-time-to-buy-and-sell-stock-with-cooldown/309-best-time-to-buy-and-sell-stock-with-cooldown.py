class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n + 2)]
        for pos in reversed(range(n)):
            for bought in reversed(range(2)):
                dp[pos][bought] = max(
                    -prices[pos] + dp[pos + 1][1],
                    dp[pos + 1][bought],
                    (prices[pos] + dp[pos + 2][0]) if bought else 0
                )
        return dp[0][0]