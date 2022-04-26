class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        
        mst = [False] * n
        mst[0] = True
        
        h = [
            (abs(points[0][0] - points[i][0]) +\
             abs(points[0][1] - points[i][1]), i)
            for i in range(1, n)
        ]
        heapify(h)
        
        ecount = cost = 0
        while ecount < n - 1:
            while mst[h[0][1]]:
                heappop(h)
            
            d, i = heappop(h)
            mst[i] = True
            cost += d
            ecount += 1
            
            for j in range(n):
                if not mst[j]:
                    heappush(h, (abs(points[i][0] - points[j][0]) +\
                                 abs(points[i][1] - points[j][1]), j))
        return cost
            