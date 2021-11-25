class DisjoinSet:
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
                
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, m = len(isConnected), len(isConnected[0])
        
        ds = DisjoinSet(n)
        for i in range(n):
            for j in range(m):
                if i != j and isConnected[i][j]:
                    ds.union(i, j)
        
        return ds.roots
        