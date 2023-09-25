class Solution(object):
    def shortestDistance(self, grid):
        def bfs(x: int, y: int) -> None:
            seen = {(x, y)}
            q = [(x, y)]
            d = 0
            while q:
                nq = []
                
                for a, b in q:
                    grid[a][b] -= d
                    counts[(a, b)] += 1
                    
                    for da, db in diff:
                        na, nb = a + da, b + db
                        
                        if 0 <= na < m and 0 <= nb < n and grid[na][nb] <= 0 and (na, nb) not in seen:
                            nq.append((na, nb))
                            seen.add((na, nb))
                d += 1
                q = nq
            
        
        m, n = len(grid), len(grid[0])
        diff = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        counts = defaultdict(int)
        
        ones = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ones += 1
                    bfs(i, j)
        
        res = [abs(grid[i][j]) for i in range(m) for j in range(n) if grid[i][j] < 0 and counts[(i, j)] == ones]
        
        return -1 if not res else min(res)