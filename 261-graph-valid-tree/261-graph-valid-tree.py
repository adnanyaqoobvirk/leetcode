class DisjointSet:
    def __init__(self: Any, n: int) -> None:
        self.nodes = [-1 for i in range(n)]
        self.roots = n
        
    def find(self, x) -> int:
        if self.nodes[x] >= 0:
            self.nodes[x] = self.find(self.nodes[x])
            return self.nodes[x]
        else:
            return x
    
    def union(self, x, y) -> None:
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
            return True
        else:
            return False

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        ds = DisjointSet(n)
        for i, j in edges:
            if not ds.union(i, j):
                return False
        
        return ds.roots == 1