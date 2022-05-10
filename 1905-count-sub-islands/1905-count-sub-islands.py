class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n, subislands = len(grid2), len(grid2[0]), 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] != 1:
                    continue
                q, grid2[i][j], is_subisland = [(i, j)], 0, True if grid1[i][j] == 1 else False
                while q:
                    nq = []
                    for a, b in q:
                        for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                            if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                                if grid1[x][y] != 1:
                                    is_subisland = False
                                grid2[x][y] = 0
                                nq.append((x, y))
                    q = nq
                if is_subisland:
                    subislands += 1
        return subislands