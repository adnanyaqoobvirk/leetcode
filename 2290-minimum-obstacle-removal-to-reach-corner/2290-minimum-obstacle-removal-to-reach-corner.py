class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = [(0, 0, 0)]
        d = defaultdict(lambda: inf)
        d[(0, 0)] = 0
        while h:
            ud, ux, uy = heappop(h)
            for vx, vy in [(ux + 1, uy), (ux - 1, uy), (ux, uy + 1), (ux, uy - 1)]:
                if 0 <= vx < m and 0 <= vy < n:
                    w = d[(ux, uy)] + grid[vx][vy]
                    if w < d[(vx, vy)]:
                        d[(vx, vy)] = w
                        heappush(h, (w, vx, vy))
        return d[(m - 1, n - 1)]