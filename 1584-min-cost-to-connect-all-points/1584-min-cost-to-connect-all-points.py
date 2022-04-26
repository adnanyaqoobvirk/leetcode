class UF:
    def __init__(self, n: int) -> None:
        self.nodes = list(range(n))
        self.rank = [0] * n
        
    def find(self, node: int) -> int:
        if self.nodes[node] != node:
            self.nodes[node] = self.find(self.nodes[node])
        return self.nodes[node]
        
    def union(self, node1: int, node2: int) -> bool:
        pnode1, pnode2 = self.find(node1), self.find(node2)
        if pnode1 == pnode2:
            return False
        
        if self.rank[pnode1] > self.rank[pnode2]:
            self.nodes[pnode2] = pnode1
        elif self.rank[pnode1] < self.rank[pnode2]:
            self.nodes[pnode1] = pnode2
        else:
            self.nodes[pnode1] = pnode2
            self.rank[pnode2] += 1
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