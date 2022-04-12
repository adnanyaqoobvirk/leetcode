from sortedcontainers import SortedDict

class Point:
    def __init__(self, left: int, height: int, start: bool) -> None:
        self.left = left
        self.height = height
        self.start = start
        
    def __lt__(self, other) -> bool:
        if self.left != other.left:
            return self.left < other.left
        elif not self.start and not other.start:
            return self.height < other.height
        elif self.start and other.start:
            return self.height > other.height
        else:
            return self.start
        
    def __repr__(self):
        return f"{self.left},{self.height},{self.start}"
        
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []
        for left, right, height in buildings:
            points.append(Point(left, height, True))
            points.append(Point(right, height, False))
        points.sort()
        
        h, max_height, ans = SortedDict({0: 1}), 0, []
        for point in points:
            if point.start:
                h[point.height] = h.get(point.height, 0) + 1
                curr_max_height = h.keys()[-1]
                if curr_max_height != max_height:
                    max_height = curr_max_height
                    ans.append([point.left, max_height])
            else:
                h[point.height] -= 1
                if h[point.height] == 0:
                    del h[point.height]
                curr_max_height = h.keys()[-1]
                if curr_max_height != max_height:
                    max_height = curr_max_height
                    ans.append([point.left, max_height])
        return ans