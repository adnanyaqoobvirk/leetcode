class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def exploreIsland(a: int, b: int) -> None:
            q = [(a, b)]
            while q:
                nq = []
                for x, y in q:
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == "1":
                        grid[x][y] = "2"
                        nq.append((x, y - 1))
                        nq.append((x, y + 1))
                        nq.append((x - 1, y))
                        nq.append((x + 1, y))
                q = nq
                
        n, m, islands = len(grid), len(grid[0]), 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    islands += 1
                    exploreIsland(i, j)
        return islands
                                
                    
                