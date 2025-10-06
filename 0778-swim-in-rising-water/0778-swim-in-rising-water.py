class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        h = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        min_time = 0
        while h:
            height, i, j = heappop(h)
            min_time = max(min_time, height)
            if i == m - 1 and j == n - 1:
                return min_time

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in seen:
                    heappush(h, (grid[x][y], x, y))
                    seen.add((x, y))
        return -1