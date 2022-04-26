class UF:
    def __init__(self, n: int) -> None:
        self.root = [-1] * n
        
    def find(self, node: int) -> int:
        if self.root[node] >= 0:
            self.root[node] = self.find(self.root[node])
            return self.root[node]
        return node
        
    def union(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        
        if self.root[root1] < self.root[root2]:
            self.root[root2] = root1
        elif self.root[root1] > self.root[root2]:
            self.root[root1] = root2
        else:
            self.root[root1] = root2
            self.root[root2] -= 1
        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges, n = [], len(points)
        for i in range(n):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((d, i, j))
        edges.sort()
        
        uf, cost, ecount = UF(n), 0, 0
        for d, i, j in edges:
            if uf.union(i, j):
                cost += d
                ecount += 1
                if ecount == n - 1:
                    break
        return cost