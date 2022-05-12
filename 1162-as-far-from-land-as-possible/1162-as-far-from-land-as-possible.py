class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, q = len(grid), []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
        
        maxd = -1
        while q:
            nq = []
            for a, b, d in q:
                for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                            nd = d + abs(a - x) + abs(b - y)
                            maxd = max(maxd, nd)
                            grid[x][y] = 1
                            nq.append((x, y, nd))
            q = nq
        return maxd