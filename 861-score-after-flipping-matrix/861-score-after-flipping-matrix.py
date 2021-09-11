class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        
        for i in range(h):
            if grid[i][0] == 0:
                for j in range(w):
                    grid[i][j] ^= 1
        
        for j in range(1, w):
            if sum(
                1 if not grid[i][j] else 0 
                for i in range(h)
            ) > (h / 2):
                for i in range(h):
                    grid[i][j] ^= 1
        
        return sum(
            2 ** (w - j - 1) 
            for i in range(h) 
            for j in range(w) 
            if grid[i][j]
        )