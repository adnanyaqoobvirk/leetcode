class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dpoints = [(point[0]**2 + point[1]**2, i) for i, point in enumerate(points)]
        heapify(dpoints)
        return [points[heappop(dpoints)[1]] for _ in range(k)]