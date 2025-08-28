class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        for j in range(1, n):
            d = []
            for i in range(m - j):
                d.append(grid[i][i + j])
            d.sort()
            for i in range(m - j):
                grid[i][i + j] = d[i]
        
        for i in range(m):
            d = []
            for j in range(n - i):
                d.append(grid[i + j][j])
            d.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = d[j]

        return grid
                