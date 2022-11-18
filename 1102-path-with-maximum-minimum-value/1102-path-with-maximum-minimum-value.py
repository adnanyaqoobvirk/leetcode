class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def possible(score):
            if grid[0][0] < score:
                return False
            
            q = [(0, 0)]
            seen = {(0, 0)}
            while q:
                nq = []
                for i, j in q:
                    if i == m - 1 and j == n - 1:
                        return True
                    
                    for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= x < m and 0 <= y < n and grid[x][y] >= score and (x, y) not in seen:
                            nq.append((x, y))
                            seen.add((x, y))
                q = nq
            return False
        
        m, n = len(grid), len(grid[0])
        
        min_score = min(min(grid[i]) for i in range(m))
        
        lo, hi = min_score, min(grid[0][0], grid[m - 1][n - 1]) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if possible(mid):
                lo = mid
            else:
                hi = mid
        return lo