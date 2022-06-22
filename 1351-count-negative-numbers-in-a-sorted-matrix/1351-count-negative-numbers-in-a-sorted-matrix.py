class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for row in range(m):
            if grid[row][0] < 0:
                ans += n * (m - row)
                break
                
            lo, hi = 0, n
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if grid[row][mid] <= -1:
                    hi = mid
                else:
                    lo = mid + 1
            ans += (n - lo)
        return ans