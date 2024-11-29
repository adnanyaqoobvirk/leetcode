class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])
        dis = defaultdict(lambda: inf)
        dis[(0, 0)] = 0
        seen = {(0, 0)}
        h = [(0, 0, 0)]
        while h:
            s, i, j = heappop(h)
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    ns = max(s + 1, grid[x][y] if s & 1 ^ grid[x][y] & 1 else grid[x][y] + 1)
                    if ns < dis[(x, y)]:
                        dis[(x, y)] = ns
                        heappush(h, (ns, x, y))
                        seen.add((x, y))
        return dis[(m - 1, n - 1)]