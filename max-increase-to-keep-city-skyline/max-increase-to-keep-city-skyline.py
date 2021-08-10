class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [None] * n
        col_max = [None] * n
        total = 0
        for i in range(n):
            if row_max[i] is None:
                row_max[i] = max(grid[i])
            for j in range(n):
                if col_max[j] is None:
                    col_max[j] = max([grid[k][j] for k in range(n)])
                total += min(row_max[i], col_max[j]) - grid[i][j]
        return total