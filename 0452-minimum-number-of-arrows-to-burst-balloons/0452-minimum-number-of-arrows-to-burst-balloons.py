class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans, pstart, pend = 1, float('-inf'), float('inf')
        for start, end in points:
            if start > pend:
                ans += 1
                pstart, pend = start, end
            else:
                pstart = max(pstart, start)
                pend = min(pend, end)
        return ans