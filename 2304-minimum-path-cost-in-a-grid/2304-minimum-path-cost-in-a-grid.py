class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        @cache
        def dp(i: int, k: int) -> int:
            if i == m:
                return 0
            
            res = inf
            for j in range(n):
                cost = 0 if i == 0 else moveCost[k][j]
                res = min(res, grid[i][j] + cost + dp(i + 1, grid[i][j]))
            return res
        
        m, n = len(grid), len(grid[0])
        return dp(0, 0)