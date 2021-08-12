class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        max_area = 0
        for i in range(len(points) - 1):
            current_area = points[i + 1][0] - points[i][0]
            if current_area > max_area:
                max_area = current_area
        return max_area