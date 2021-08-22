class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxLen = 0
        maxLenCounts = 0
        for l, w in rectangles:
            side = min(l, w)
            if side > maxLen:
                maxLen = side
                maxLenCounts = 1
            elif side == maxLen:
                maxLenCounts += 1
        return maxLenCounts