class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parents = [[(i, j) for j in range(n)] for i in range(m)]
        rank = [[0] * n for _ in range(m)]
        
        def find(i: int, j: int) -> Tuple[int, int]:
            if parents[i][j] != (i, j):
                parents[i][j] = find(*parents[i][j])
            return parents[i][j]
    
        def union(i: int, j: int, x: int, y: int) -> bool:
            pp, qp = find(i, j), find(x, y)
            
            if pp == qp:
                return False
            
            if rank[pp[0]][pp[1]] == rank[qp[0]][qp[1]]:
                parents[qp[0]][qp[1]] = pp
                rank[pp[0]][pp[1]] += 1
            elif rank[pp[0]][pp[1]] > rank[qp[0]][qp[1]]:
                parents[qp[0]][qp[1]] = pp
            else:
                parents[pp[0]][pp[1]] = qp
                
            return True
        
        res = []
        islands = 0
        grid = [[False] * n for _ in range(m)]
        for i, j in positions:
            if not grid[i][j]:
                grid[i][j] = True
                islands += 1
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == True:
                        if union(i, j, x, y):
                            islands -= 1
            res.append(islands)
        return res