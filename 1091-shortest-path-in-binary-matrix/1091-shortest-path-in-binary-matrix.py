class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        
        n, m = len(grid), len(grid[0])
        sides = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        done, q = {(0, 0)}, [[0, 0, 1]]
        while q:
            nq = []
            for x, y, l in q:
                if x == n - 1 and y == m - 1:
                    return l
                
                for i, j in sides:
                    if 0 <= x + i < n and 0 <= y + j < m and (x + i, y + j) not in done and not grid[x + i][y + j]:
                        done.add((x + i, y + j))
                        nq.append([x + i, y + j, l + 1])
            q = nq
        return -1