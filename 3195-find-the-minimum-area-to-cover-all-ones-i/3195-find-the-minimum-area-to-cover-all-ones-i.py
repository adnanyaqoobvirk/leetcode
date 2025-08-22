class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minx, maxx, miny, maxy = inf, 0, inf, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    minx, maxx = min(minx, i), max(maxx, i)
                    miny, maxy = min(miny, j), max(maxy, j)
        return (maxx - minx + 1) * (maxy - miny + 1)