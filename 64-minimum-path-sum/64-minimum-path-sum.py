class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m - 1 and j == n - 1:
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    )
        return dp[0][0]