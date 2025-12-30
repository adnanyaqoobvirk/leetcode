class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        res = []
        for j in range(n):
            max_len = 0
            for i in range(m):
                max_len = max(max_len, len(str(grid[i][j])))
            res.append(max_len)
        return res