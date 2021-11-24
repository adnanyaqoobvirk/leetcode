class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        ans = []
        p1 = p2 = 0
        while p1 < n and p2 < m:
            p1start, p1end = firstList[p1]
            p2start, p2end = secondList[p2]
            
            if p1end >= p2end:
                p2 += 1
            else:
                p1 += 1
                
            lo, hi = max(p1start, p2start), min(p1end, p2end)
            if lo <= hi:
                ans.append([lo, hi])
        return ans