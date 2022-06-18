class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        vpoints = [
            (abs(x - px) + abs(y - py), i)
            for i, (px, py) in enumerate(points)
            if px == x or py == y
        ]
        
        if not vpoints:
            return -1
        
        vpoints.sort()
        return vpoints[0][1]