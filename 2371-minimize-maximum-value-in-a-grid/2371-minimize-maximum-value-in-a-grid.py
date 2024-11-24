class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        nums = sorted((grid[i][j], i, j) for i in range(m) for j in range(n))
        rmax = defaultdict(int)
        cmax = defaultdict(int)
        r = 0
        ans = [row[::] for row in grid]
        for num, i, j in nums:
            p = max(rmax[i], cmax[j]) + 1
            for a, b in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= a < m and 0 <= b < n and ans[a][b] <= r:
                    p = max(p, ans[a][b] + 1)
            ans[i][j] = p
            rmax[i] = p
            cmax[j] = p
            r = max(r, p)
        return ans