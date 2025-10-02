class UF:
    def __init__(self, n: int) -> None:
        self.roots = list(range(n + 1))
        self.rank = [0] * (n + 1)
    
    def find(self, x) -> int:
        if self.roots[x] != x:
            self.roots[x] = self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y) -> bool:
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.roots[rootY] = rootX
                self.rank[rootX] += 1
            else:
                self.roots[rootX] = rootY
                self.rank[rootY] += 1
            return True
        
        return False

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda x: x[2])

        uf = UF(n)
        min_cost = 0
        edge_count = 0
        
        for x, y, cost in connections:
            if uf.union(x, y):
                min_cost += cost
                edge_count += 1
        
        if edge_count == n - 1:
            return min_cost
        
        return -1