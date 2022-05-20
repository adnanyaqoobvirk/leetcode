class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if (i == m - 1 and j == n - 1) or obstacleGrid[i][j] == 1:
                    continue
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]
        return dp[0][0]