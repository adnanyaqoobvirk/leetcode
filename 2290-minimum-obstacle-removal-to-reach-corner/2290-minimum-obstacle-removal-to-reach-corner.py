class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        tx, ty = m - 1, n - 1
        cells = m * n + 1
        h = [(0, 0, 0)]
        d = defaultdict(lambda: inf)
        d[(0, 0)] = 0
        while h:
            ud, ux, uy = heappop(h)

            if ux == tx and uy == ty:
                return floor(ud / cells)

            for vx, vy in [(ux + 1, uy), (ux - 1, uy), (ux, uy + 1), (ux, uy - 1)]:
                if 0 <= vx < m and 0 <= vy < n:
                    w = d[(ux, uy)] + (1 if grid[vx][vy] == 0 else cells)
                    if w < d[(vx, vy)]:
                        d[(vx, vy)] = w
                        heappush(h, (w, vx, vy))
        return -1