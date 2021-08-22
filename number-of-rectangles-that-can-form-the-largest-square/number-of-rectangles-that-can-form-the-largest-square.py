class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        lenCounts = {}
        maxLen = 0
        maxLenCounts = 0
        for l, w in rectangles:
            side = min(l, w)
            lenCounts[side] = lenCounts.get(side, 0) + 1
            if side >= maxLen:
                maxLen = side
                maxLenCounts = lenCounts[side]
        return maxLenCounts