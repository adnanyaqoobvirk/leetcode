class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[-inf] * (k + 2) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                for r in reversed(range(k + 1)):
                    cost = 1 if grid[i][j] == 2 else grid[i][j]
                    score = grid[i][j]

                    if r - cost < 0:
                        continue

                    if i == m - 1 and j == n - 1:
                        dp[i][j][r] = score
                        continue
            
                    dp[i][j][r] = score + max(dp[i][j + 1][r - cost], dp[i + 1][j][r - cost])
        return -1 if dp[0][0][k] == -inf else dp[0][0][k]