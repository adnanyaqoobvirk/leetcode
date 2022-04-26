class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        mst = [False] * n
        h = [
            (abs(points[0][0] - points[i][0]) + abs(points[0][1] - points[i][1]), 0, i)
            for i in range(1, n)
        ]
        heapify(h)
        
        ecount = cost = 0
        while ecount < n - 1:
            while mst[h[0][1]] and mst[h[0][2]]:
                heappop(h)
            d, i, j = heappop(h)
            mst[i] = mst[j] = True
            cost += d
            ecount += 1
            for k in range(n):
                if k != j and not mst[k]:
                    heappush(h, (abs(points[j][0] - points[k][0]) + abs(points[j][1] - points[k][1]), j, k))
        return cost
            