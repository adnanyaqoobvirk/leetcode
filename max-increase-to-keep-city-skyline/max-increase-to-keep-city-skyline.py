class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        row_max = [max(grid[i]) for i in range(n)]
        col_max = [max([grid[i][j] for i in range(n)]) for j in range(n)]
        return sum([min(row_max[i], col_max[j]) - grid[i][j] for i in range(n) for j in range(n)])