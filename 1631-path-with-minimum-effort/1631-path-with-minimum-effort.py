class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def valid(i: int, j: int, effort: int) -> bool:
            if i == m - 1 and j == n - 1:
                return True
            
            for di, dj in neighbors:
                x, y = i + di, j + dj

                if 0 <= x < m and 0 <= y < n and (x, y) not in seen and abs(heights[i][j] - heights[x][y]) <= effort:
                    seen.add((x, y))
                    if valid(x, y, effort):
                        return True
            
            return False
        
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        m, n = len(heights), len(heights[0])
        
        lo, hi = -1, max(max(row) for row in heights)
        while lo + 1 < hi:
            mid = lo + hi >> 1
            
            seen = {(0, 0)}
            
            if valid(0, 0, mid):
                hi = mid
            else:
                lo = mid
        return hi