class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n, paths = len(grid), len(grid[0]), set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                q, path, grid[i][j] = [(i, j)], [], 0
                while q:
                    nq = []
                    for a, b in q:
                        for x, y, p in [
                            (a, b - 1, 'L'), 
                            (a, b + 1, 'R'), 
                            (a - 1, b, 'U'), 
                            (a + 1, b, 'D')
                        ]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                                grid[x][y] = 0
                                path.append(p)
                                nq.append((x, y))
                        path.append('|')
                    q = nq
                paths.add("".join(path))
        return len(paths)