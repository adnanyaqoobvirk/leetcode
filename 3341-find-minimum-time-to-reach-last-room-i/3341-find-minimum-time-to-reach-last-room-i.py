class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        dmap = defaultdict(lambda: inf)
        h = [(0, 0, 0)]
        while h:
            d, i, j = heappop(h)
            if dmap[(i, j)] < d:
                continue
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and max(moveTime[x][y] + 1, d + 1) < dmap[(x, y)]:
                    dmap[(x, y)] = max(moveTime[x][y] + 1, d + 1)
                    heappush(h, (dmap[(x, y)], x, y))
        return dmap[(n - 1, m - 1)]