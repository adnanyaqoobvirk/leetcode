class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n, directions, stack = len(grid), [(0, -1), (0, 1), (-1, 0), (1, 0)], []
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    stack.append((i, j))
                    break
            else:
                continue
            break
            
        q = []
        while stack:
            i, j = stack.pop()
            q.append((i, j, 0))
            grid[i][j] = -1
            for x, y in directions:
                x, y = i + x, j + y
                if 0 <= x < n and 0 <= y < n:
                    if grid[x][y] == 1:
                        grid[x][y] = 0
                        stack.append((x, y))
                        
        while q:
            nq = []
            for i, j, d in q:
                for x, y in directions:
                    x, y = i + x, j + y
                    if 0 <= x < n and 0 <= y < n and grid[x][y] != -1:
                        if grid[x][y] == 1:
                            return d
                        grid[x][y] = -1
                        nq.append((x, y, d + 1))
            q = nq