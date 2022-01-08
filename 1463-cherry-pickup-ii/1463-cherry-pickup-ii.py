class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @cache
        def helper(i: int, j: int, k: int) -> int:
            if i >= n or j < 0 or j >= m or k < 0 or k >= m or j >= k:
                return 0

            cherries = grid[i][j] + grid[i][k]
            
            max_cherries = 0
            for a in [j, j + 1, j - 1]:
                for b in [k, k + 1, k - 1]:
                    max_cherries = max(max_cherries, helper(i + 1, a, b))
            
            return cherries + max_cherries
        
        n, m = len(grid), len(grid[0])
        return helper(0, 0, m - 1)