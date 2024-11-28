class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ti, tj = m - 1, n - 1
        obs = defaultdict(lambda: inf)
        obs[(0, 0)] = 0
        q = deque([(0, 0)])
        while q:
            i, j = q.popleft()
            if i == ti and j == tj:
                return obs[(i, j)]
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and obs[(x, y)] == inf:
                    if grid[x][y] == 1:
                        q.append((x, y))
                        obs[(x, y)] = obs[(i, j)] + 1
                    else:
                        q.appendleft((x, y))
                        obs[(x, y)] = obs[(i, j)]
        return -1
            