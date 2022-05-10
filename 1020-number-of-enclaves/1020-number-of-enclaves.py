class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, ans = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                stack, lands, grid[i][j] = [(i, j)], 0, 0
                boundry = True if i == 0 or i == m - 1 or j == 0 or j == n - 1 else False
                while stack:
                    a, b = stack.pop()
                    for x, y in [(a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                            if not boundry:
                                boundry = (
                                    True 
                                    if x == 0 or x == m - 1 or y == 0 or y == n - 1 
                                    else False
                                )
                            grid[x][y] = 0
                            stack.append((x, y))
                    lands += 1
                if not boundry:
                    ans += lands
        return ans
                