class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        prev, curr = [float('inf')] * (n + 1), [float('inf')] * (n + 1)
        prev[n - 1] = 0
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                curr[j] = grid[i][j] + min(
                    prev[j],
                    curr[j + 1]
                )
            prev, curr = curr, prev
        return prev[0]