class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i**2 for i in range(int(math.sqrt(n)) + 1)]
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            min_square = float('inf')
            for j in range(1, int(math.sqrt(i)) + 1):
                min_square = min(dp[i - squares[j]] + 1, min_square)
            dp[i] = min_square
        return dp[n]