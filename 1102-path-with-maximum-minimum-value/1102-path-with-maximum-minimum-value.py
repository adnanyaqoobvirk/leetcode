class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        def pathExists(score: int) -> int:
            q = [(0, 0)]
            processed = {(0, 0)}
            while q:
                nq = []
                for i, j in q:
                    if i == m - 1 and j == n - 1:
                        return True
                    for x, y in [(i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) not in processed and grid[x][y] >= score:
                            processed.add((x, y))
                            nq.append((x, y))
                q = nq
            return False
                        
        m, n = len(grid), len(grid[0])
        lo, hi = 0, min(grid[0][0], grid[m - 1][n - 1])
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if pathExists(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return lo if pathExists(lo) else lo - 1