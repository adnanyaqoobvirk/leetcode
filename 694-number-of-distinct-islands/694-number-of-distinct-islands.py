class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n, islands = len(grid), len(grid[0]), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                q, left, top, island, grid[i][j] = [(i, j)], i, j, [(i, j)], 0
                while q:
                    nq = []
                    for a, b in q:
                        for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                                left, top, grid[x][y] = min(left, x), min(top, y), 0
                                island.append((x, y))
                                nq.append((x, y))
                    q = nq
                islands.add(tuple((i - left, j - top) for i, j in island))
        return len(islands)