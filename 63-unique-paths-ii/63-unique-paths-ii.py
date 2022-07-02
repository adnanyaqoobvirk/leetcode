class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or obstacleGrid[i][j] == 1:
                return 0
            
            if i == m - 1 and j == n - 1:
                return 1
            
            return helper(i + 1, j) + helper(i, j + 1)
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        return helper(0, 0)