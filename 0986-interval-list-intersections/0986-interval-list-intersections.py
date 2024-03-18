class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        n = len(firstList)
        m = len(secondList)
        
        ans = []
        p1 = 0
        p2 = 0
        
        while p1 < n and p2 < m:
            lo = max(firstList[p1][0], secondList[p2][0])
            hi = min(firstList[p1][1], secondList[p2][1])
            if lo <= hi:
                ans.append([lo, hi])
                
            if firstList[p1][1] <= secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        
        return ans