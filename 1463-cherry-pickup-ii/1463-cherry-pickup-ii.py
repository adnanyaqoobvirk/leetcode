class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = [[[0] * (m + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                for k in range(m):
                    max_cherries = 0
                    for a in [j, j + 1, j - 1]:
                        for b in [k, k + 1, k - 1]:
                            if b > a:
                                max_cherries = max(max_cherries, dp[i + 1][a][b])
                    dp[i][j][k] = grid[i][j] + grid[i][k] + max_cherries
        return dp[0][0][m - 1]