class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        x_p = self.find(x)
        y_p = self.find(y)
        
        if x_p == y_p:
            return False
        
        if self.rank[x_p] == self.rank[y_p]:
            self.parent[x_p] = y_p
            self.rank[y_p] += 1
        elif self.rank[x_p] < self.rank[y_p]:
            self.parent[x_p] = y_p
        else:
            self.parent[y_p] = x_p
        
        return True
            
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        ds = DisjointSet(m * n)
        
        res = []
        islands = 0
        grid = [[False] * n for _ in range(m)]
        for i, j in positions:
            if not grid[i][j]:
                grid[i][j] = True
                islands += 1
                for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == True:
                        if ds.union(i * n + j, x * n + y):
                            islands -= 1
            res.append(islands)
        return res