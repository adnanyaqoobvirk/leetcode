class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        lands = {
            (i, j) 
            for i in range(m) 
            for j in range(n) 
            if grid[i][j] == '1'
        }
        
        ans = 0
        while lands:
            q = [lands.pop()]
            while q:
                nq = []
                for i, j in q:
                    for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                        if 0 <= x < m and 0 <= y < n and (x, y) in lands:
                            lands.discard((x, y))
                            nq.append((x, y))
                q = nq
            ans += 1
        return ans