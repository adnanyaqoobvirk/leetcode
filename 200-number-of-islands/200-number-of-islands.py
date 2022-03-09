class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m, islands = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    grid[i][j] = "2"
                    
                    q = [(i,j)]
                    while q:
                        nq = []
                        for x, y in q:
                            for a, b in [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]:
                                if 0 <= a < n and 0 <= b < m and grid[a][b] == "1":    
                                    grid[a][b] = "2"
                                    nq.append((a, b))
                        q = nq
        return islands
                                
                    
                