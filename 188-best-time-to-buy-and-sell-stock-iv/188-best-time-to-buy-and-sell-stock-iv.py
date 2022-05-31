class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[[0] * (k + 1) for _ in range(2)] for _ in range(n + 1)]
        for pos in reversed(range(n)):
            for bought in reversed(range(2)):
                for t in range(1, k + 1):
                    buy_stock = 0
                    if not bought:
                        buy_stock = -prices[pos] + dp[pos + 1][1][t]

                    skip = dp[pos + 1][bought][t]

                    sell_stock = 0
                    if bought:
                        sell_stock = prices[pos] + dp[pos + 1][0][t - 1]

                    dp[pos][bought][t] = max(
                        buy_stock,
                        skip,
                        sell_stock
                    )
        return dp[0][0][k]