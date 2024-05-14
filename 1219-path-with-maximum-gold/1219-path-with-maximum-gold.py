class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def backtrack(i, j):
            grid[i][j] = -grid[i][j]
            ans = 0
            for x, y in nei:
                x, y = x + i, y + j
                if 0 <= x < m and 0 <= y < n and grid[x][y] > 0:
                    ans = max(ans, grid[x][y] + backtrack(x, y))
            grid[i][j] = -grid[i][j]
            return ans
        
        m, n = len(grid), len(grid[0])
        nei = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        ans = 0
        for a in range(m):
            for b in range(n):
                if grid[a][b] > 0:
                    ans = max(ans, grid[a][b] + backtrack(a, b))
        return ans