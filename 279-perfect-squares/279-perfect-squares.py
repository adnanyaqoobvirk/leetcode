class Solution:
    def numSquares(self, n: int) -> int:
        squares = [num ** 2 for num in range(1, math.ceil(math.sqrt(n)) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        for total in reversed(range(n)):
            for square in reversed(squares):
                ntotal = total + square
                if ntotal <= n:
                    dp[total] = min(dp[total], 1 + dp[ntotal])
        return dp[0]