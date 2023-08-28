class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ones = set((i, j) for i in range(m) for j in range(n) if grid[i][j] == '1')
        res = 0
        while ones:
            q = [ones.pop()]
            while q:
                nq = []
                for i, j in q:
                    for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) in ones:
                            nq.append((x, y))
                            ones.remove((x, y))
                q = nq
            res += 1
        return res
                