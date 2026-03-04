class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        curr, prev = [inf] * (m * n), [0] * (m * n)
        for i in reversed(range(m)):
            for k in range(m * n):
                for j in range(n):
                    cost = 0 if i == 0 else moveCost[k][j]
                    curr[k] = min(curr[k], grid[i][j] + cost + prev[grid[i][j]])
            prev, curr = curr, [inf] * (m * n)
        return prev[0]