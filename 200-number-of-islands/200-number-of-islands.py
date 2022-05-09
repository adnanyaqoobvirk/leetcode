class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, islands = len(grid), len(grid[0]), 0
        for a in range(m):
            for b in range(n):
                if grid[a][b] != '1':
                    continue
                grid[a][b] = '0'
                q = [(a, b)]
                while q:
                    nq = []
                    for i, j in q:
                        for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                                grid[x][y] = '0'
                                nq.append((x, y))
                    q = nq
                islands += 1
        return islands