class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0:
            return -1
        
        n, q, ans = len(grid), [(0, 0)], 1
        ne = [
            (-1, -1),(-1, 0),(-1, 1),
            (0, -1),(0, 1),
            (1, -1),(1, 0),(1, 1)
        ]
        while q:
            nq = []
            for i, j in q:
                if i == n - 1 and j == n - 1:
                    return ans
                for x, y in ne:
                    x, y = i + x, j + y
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0:
                        grid[x][y] = 1
                        nq.append((x, y))
            q = nq
            ans += 1
        return -1