class UF:
    def __init__(self, n):
        self.nodes = [i for i in range(n)]
    
    def find(self, i) -> int:
        if self.nodes[i] == i:
            return i
        else:
            self.nodes[i] = self.find(self.nodes[i])
            return self.nodes[i]
    
    def union(self, i, j):
        pi, pj = self.find(i), self.find(j)
        if pi != pj: self.nodes[pj] = pi
            
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                (pix, piy), (pjx, pjy) = points[i], points[j]
                edges.append((abs(pix - pjx) + abs(piy - pjy), (i, j)))
        edges.sort(key=lambda x: x[0])
        
        ans = ecount = 0
        uf = UF(len(points))
        for d, (i, j) in edges:
            if uf.find(i) != uf.find(j):
                uf.union(i, j)
                ans += d
                ecount += 1
                if ecount == len(points) - 1:
                    break
        return ans