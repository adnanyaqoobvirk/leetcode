class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(effort: int) -> bool:
            seen = {(0, 0)}
            q = [(0, 0)]
            while q:
                nq = []
                for i, j in q:
                    if i == m - 1 and j == n - 1:
                        return True
                    
                    for di, dj in neighbors:
                        x, y = i + di, j + dj
                        
                        if 0 <= x < m and 0 <= y < n and (x, y) not in seen and abs(heights[i][j] - heights[x][y]) <= effort:
                            nq.append((x, y))
                            seen.add((x, y))
                q = nq
            return False
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m, n = len(heights), len(heights[0])
        
        lo, hi = -1, 10 ** 6
        while lo + 1 < hi:
            mid = lo + hi >> 1
            
            if valid(mid):
                hi = mid
            else:
                lo = mid
        return hi