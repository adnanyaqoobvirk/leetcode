class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = {(i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"}
        
        islands = 0
        while ones:
            q = [ones.pop()]
            while q:
                nq = []
                for i, j in q:
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) in ones and grid[x][y] == "1":
                            ones.remove((x, y))
                            nq.append((x, y))
                q = nq
            islands += 1
        return islands