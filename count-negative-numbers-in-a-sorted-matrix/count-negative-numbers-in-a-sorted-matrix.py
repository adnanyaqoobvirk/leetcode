class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        count = 0
        for i in range(n):
            if grid[i][0] < 0:
                count += (n - i) * m
                break
            else:
                for j in range(m):
                    if grid[i][j] < 0:
                        count += (m - j)
                        break
        return count