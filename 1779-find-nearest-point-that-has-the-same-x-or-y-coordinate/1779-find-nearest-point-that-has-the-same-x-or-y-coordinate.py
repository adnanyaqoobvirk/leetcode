class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dis, min_idx = inf, -1
        for i, (px, py) in enumerate(points):
            if px == x or py == y:
                dis = abs(px - x) + abs(py - y)
                if dis < min_dis:
                    min_dis, min_idx = dis, i
        return min_idx