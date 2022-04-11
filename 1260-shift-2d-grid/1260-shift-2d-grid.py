class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for _ in range(k):
            last_col = []
            for row in grid:
                last_col.append(row.pop())
            
            grid[0].insert(0, last_col.pop())
            for i in range(1, m):
                grid[i].insert(0, last_col[i - 1])
        return grid