class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n, max_island = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                q, island, grid[i][j] = [(i, j)], 1, 0
                while q:
                    nq = []
                    for a, b in q:
                        for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                                grid[x][y] = 0
                                nq.append((x, y))
                    q = nq
                    island += len(nq)
                max_island = max(max_island, island)
        return max_island