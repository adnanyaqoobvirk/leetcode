class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        curr, prev = [0] * (m * n), [0] * (m * n)
        for i in reversed(range(m)):
            for k in range(m * n):
                res = inf
                for j in range(n):
                    cost = 0 if i == 0 else moveCost[k][j]
                    res = min(res, grid[i][j] + cost + prev[grid[i][j]])
                curr[k] = res
            prev, curr = curr, prev
        return prev[0]