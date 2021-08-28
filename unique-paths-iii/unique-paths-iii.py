class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def backtrack(x: int, y: int) -> int:
            if x < 0 or x > n or y < 0 or y > m or grid[x][y] == -1:
                return 0
            
            result = len(path) == walkable and grid[x][y] == 2
            for i, j in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
                if (i, j) not in path:
                    path.add((i, j))
                    result += backtrack(i, j)
                    path.remove((i, j))
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
        path = {start}
        return backtrack(*start)
    