class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for point in points:
            t = (-1 * (point[0]**2 + point[1]**2), point)
            if len(h) == k:
                heappushpop(h, t)
            else:
                heappush(h, t)
        return [point for _, point in h]