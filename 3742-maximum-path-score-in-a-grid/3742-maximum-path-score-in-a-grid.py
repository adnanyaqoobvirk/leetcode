class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        curr, prev = [[-inf] * (k + 2) for _ in range(n + 1)], [[-inf] * (k + 2) for _ in range(n + 1)]
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                for r in reversed(range(k + 1)):
                    cost = 1 if grid[i][j] == 2 else grid[i][j]
                    score = grid[i][j]

                    if r - cost < 0:
                        continue

                    if i == m - 1 and j == n - 1:
                        curr[j][r] = score
                        continue
            
                    curr[j][r] = score + max(curr[j + 1][r - cost], prev[j][r - cost])
            prev, curr = curr, [[-inf] * (k + 2) for _ in range(n + 1)]
        return -1 if prev[0][k] == -inf else prev[0][k]