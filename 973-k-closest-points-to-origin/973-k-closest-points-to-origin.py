class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dpoints = []
        for i, (x, y) in enumerate(points):
            heappush(dpoints, (-(x**2 + y**2), i))
            while len(dpoints) > k:
                heappop(dpoints)
        return [points[i] for _, i in dpoints]