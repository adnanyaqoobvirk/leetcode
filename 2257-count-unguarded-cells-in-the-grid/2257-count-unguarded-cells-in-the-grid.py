class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = 1
        
        for i, j in guards:
            grid[i][j] = 2
            for y in range(j - 1, -1, -1):
                if grid[i][y] > 0:
                    break
                grid[i][y] = -1
                
            for y in range(j + 1, n):
                if grid[i][y] > 0:
                    break
                grid[i][y] = -1
                
            for x in range(i - 1, -1, -1):
                if grid[x][j] > 0:
                    break
                grid[x][j] = -1
                
            for x in range(i + 1, m):
                if grid[x][j] > 0:
                    break
                grid[x][j] = -1
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ans += 1
        return ans
            