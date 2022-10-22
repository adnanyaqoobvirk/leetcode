class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[-inf] * (n + 1) for _ in range(2)]
        for i in reversed(range(n)):
            for bought in range(2):
                if bought:
                    dp[1][i] = max(
                        prices[i],
                        dp[1][i + 1]
                    )
                else:
                    dp[0][i] = max(
                        dp[0][i + 1],
                        dp[1][i + 1] - prices[i]
                    )
        return 0 if dp[0][0] < 0 else dp[0][0]