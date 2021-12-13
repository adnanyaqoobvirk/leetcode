from heapq import heapify, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(x: int) -> int:
            if nodes[x] != x:
                nodes[x] = find(nodes[x])
            return nodes[x]
        
        n = len(points)
        edges = [            
            (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j)
            for i in range(n)
            for j in range(i + 1, n)
        ]
        heapify(edges)
        
        nodes = [i for i in range(n)]
        min_cost = edge_count = 0
        while edge_count < n - 1:
            d, i, j = heappop(edges)
            pi, pj = find(i), find(j)
            if pi != pj:
                nodes[pj] = pi
                min_cost += d
                edge_count += 1
        return min_cost