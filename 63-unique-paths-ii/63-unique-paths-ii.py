class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        prev, curr = [0] * (n + 1), [0] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if obstacleGrid[i][j] == 1:
                    continue
                    
                if i == m - 1 and j == n - 1:
                    curr[j] = 1
                else:
                    curr[j] = prev[j] + curr[j + 1]
            prev, curr = curr, [0] * (n + 1)
        return prev[0]