class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i: int, j: int, d: int, turn: bool, t: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != t:
                return 0
            
            res = 1 + dp(i + dirs[d][0], j + dirs[d][1], d, turn, 2 - t)
            if turn:
                nd = (d + 1) % 4
                res = max(res, 1 + dp(i + dirs[nd][0], j + dirs[nd][1], nd, False, 2 - t))
            
            return res
        
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])
        ans = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    for k in range(4):
                        ans = max(ans, 1 + dp(x + dirs[k][0], y + dirs[k][1], k, True, 2))
        return ans