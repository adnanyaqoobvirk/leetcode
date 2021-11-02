class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x: int, y: int, count: int) -> int:
            result = 0
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if i < 0 or i > n or j < 0 or j > m or grid[i][j] == -1:
                    continue

                if count == walkable and grid[i][j] == 2:
                    result += 1
                    continue

                if grid[i][j] != 1:
                    old_val, grid[i][j] = grid[i][j], 1
                    result += backtrack(i, j, count + 1)
                    grid[i][j] = old_val
            return result
        
        n, m = len(grid) - 1, len(grid[0]) - 1
        start = None
        walkable = 0
        for i in range(n + 1):
            for j in range(m + 1):
                if grid[i][j] == 1:
                    start = (i, j)
                if grid[i][j] != -1:
                    walkable += 1
        return backtrack(*start, 2)