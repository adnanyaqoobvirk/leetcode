class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIslands(a: int, b: int) -> None:
            grid[a][b] = '2'
            for x, y in [(a, b - 1), (a, b + 1), (a + 1, b), (a - 1, b)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] == '1':
                    exploreIslands(x, y)
        
        islands, n, m = 0, len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    islands += 1
                    exploreIslands(i, j)
        return islands