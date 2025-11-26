class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                for x in range(k):
                    r = (grid[i][j] + x) % k
                    if i == m - 1 and j == n - 1:
                        dp[i][j][x] = 1 if r == 0 else 0
                    else:
                        dp[i][j][x] = (dp[i + 1][j][r] + dp[i][j + 1][r]) % MOD
        return dp[0][0][0]