class UF:
    def __init__(self, size: int) -> None:
        self.roots = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, node: int) -> int:
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]
    
    def union(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.roots[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.roots[root1] = root2
        else:
            self.roots[root1] = root2
            self.rank[root2] += 1
        return True
    
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = [(wells[i], 0, i + 1) for i in range(n)]
        for src, dest, cost in pipes:
            edges.append((cost, src, dest))
        edges.sort()
        
        uf, min_cost = UF(n + 1), 0
        for cost, src, dest in edges:
            if uf.union(src, dest):
                min_cost += cost
        return min_cost