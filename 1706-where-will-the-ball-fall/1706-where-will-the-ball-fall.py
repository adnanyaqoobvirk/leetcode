class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def helper(r: int, c: int) -> int:
            if r >= m:
                return c
            
            if grid[r][c] == 1:
                if c == n - 1 or grid[r][c + 1] == -1:
                    return -1
                else:
                    return helper(r + 1, c + 1)
            else:
                if c == 0 or grid[r][c - 1] == 1:
                    return -1
                else:
                    return helper(r + 1, c - 1)
        
        m, n = len(grid), len(grid[0])
        return [helper(0, col) for col in range(n)]