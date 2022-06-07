class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev, curr = [float('inf')] * (n + 1), [float('inf')] * (n + 1)
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if i == m - 1 and j == n - 1:
                    curr[j] = grid[i][j]
                else:
                    curr[j] = grid[i][j] + min(
                        prev[j],
                        curr[j + 1]
                    )
            prev, curr = curr, [float('inf')] * (n + 1)
        return prev[0]