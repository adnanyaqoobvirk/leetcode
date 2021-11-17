class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def helper(x: int, y: int) -> int:
            if x >= m or y >= n:
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1
            
            return helper(x + 1, y) + helper(x, y + 1)
        return helper(0, 0)