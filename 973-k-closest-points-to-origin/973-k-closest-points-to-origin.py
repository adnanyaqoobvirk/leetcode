class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dpoints = [(-(points[i][0]**2 + points[i][1]**2), i) for i in range(k)]
        heapify(dpoints)
        for i in range(k, len(points)):
            d = -(points[i][0]**2 + points[i][1]**2)
            if d > dpoints[0][0]:
                heappushpop(dpoints, (d, i))
        return [points[i] for _, i in dpoints]