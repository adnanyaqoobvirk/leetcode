class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1
        for i in range(m):
            for j in range(n):
                if (i + 1 == 1 and j + 1 == 1) or obstacleGrid[i][j] == 1:
                    continue
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
        return dp[m][n]