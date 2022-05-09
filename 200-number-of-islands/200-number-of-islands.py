class UF:
    def __init__(self, grid: List[List[str]]) -> None:
        self.cnt, self.roots, self.rank = 0, [], []
        for i in range(len(grid)):
            root, rank = [], []
            for j in range(len(grid[0])):
                root.append((i, j))
                rank.append(0)
                if grid[i][j] == '1':
                    self.cnt += 1
            self.roots.append(root)
            self.rank.append(rank)
        
    def find(self, x: int, y: int) -> Tuple[int, int]:
        if self.roots[x][y] != (x, y):
            self.roots[x][y] = self.find(*self.roots[x][y])
        return self.roots[x][y]
    
    def union(self, x1: int, y1: int, x2: int, y2: int) -> None:
        (rx1, ry1), (rx2, ry2) = self.find(x1, y1), self.find(x2, y2)
        
        if (rx1, ry1) != (rx2, ry2):
            if self.rank[rx1][ry1] > self.rank[rx2][ry2]:
                self.roots[rx1][ry1] = (rx2, ry2)
            elif self.rank[rx1][ry1] < self.rank[rx2][ry2]:
                self.roots[rx2][ry2] = (rx1, ry1)
            else:
                self.roots[rx2][ry2] = (rx1, ry1)
                self.rank[rx1][ry1] += 1
            self.cnt -= 1
        
    def count(self) -> int:
        return self.cnt
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n, uf = len(grid), len(grid[0]), UF(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '1':
                    continue
                grid[i][j] = '0'
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        uf.union(i, j, x, y)
        return uf.count()