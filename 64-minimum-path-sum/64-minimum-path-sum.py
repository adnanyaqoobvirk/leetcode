class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def helper(i: int, j: int) -> int:
            if i >= m or j >= n:
                return float('inf')
            
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            
            return grid[i][j] + min(
                helper(i + 1, j),
                helper(i, j + 1)
            )
        m, n = len(grid), len(grid[0])
        return helper(0, 0)