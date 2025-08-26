class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxd = 0
        maxa = 0
        for l, w in dimensions:
            currd = l**2 + w**2
            if currd > maxd:
                maxd = currd
                maxa = l * w
            elif currd == maxd:
                maxa = max(maxa, l * w)
        return maxa