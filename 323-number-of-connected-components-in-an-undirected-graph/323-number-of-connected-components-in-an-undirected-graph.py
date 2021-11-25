class DisjointSet:
    def __init__(self: 'DisjointSet', n: int) -> None:
        self.nodes = [-1 for i in range(n)]
        self.roots = n
    
    def find(self: 'DisjointSet', x: int) -> int:
        if self.nodes[x] >= 0:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]
        else:
            return x
    
    def union(self: 'DisjointSet', x: int, y: int) -> None:
        xp, yp = self.find(x), self.find(y)
        if xp != yp:
            if self.nodes[xp] < self.nodes[yp]:
                self.nodes[yp] = xp
            elif self.nodes[xp] > self.nodes[yp]:
                self.nodes[xp] = yp
            else:
                self.nodes[xp] = yp
                self.nodes[yp] -= 1
            self.roots -= 1
        
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = DisjointSet(n)
        for i, j in edges:
            ds.union(i, j)
        return ds.roots