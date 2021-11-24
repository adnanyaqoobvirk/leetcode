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
                
            if p1start > p2start:
                p1start, p1end, p2start, p2end = p2start, p2end, p1start, p1end
            
            if p1start <= p2start <= p1end:
                if p2end <= p1end:
                    ans.append([p2start, p2end])
                else:
                    ans.append([p2start, p1end])
        return ans