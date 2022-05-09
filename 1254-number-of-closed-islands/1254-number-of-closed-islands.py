class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n, islands = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                q = [(i, j)] 
                closed = (
                    False 
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1 
                    else True
                )
                while q:
                    nq = []
                    for a, b in q:
                        for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                                closed = (
                                    False 
                                    if x == 0 or x == m - 1 or y == 0 or y == n - 1 
                                    else closed
                                )
                                grid[x][y] = 1
                                nq.append((x, y))
                    q = nq
                if closed:
                    islands += 1
        return islands