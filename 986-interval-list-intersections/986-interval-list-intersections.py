class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        firstList.extend(secondList)
        firstList.sort()
    
        ans = []
        prev = 0
        for i in range(1, len(firstList)):
            pstart, pend = firstList[prev]
            cstart, cend = firstList[i]
            if pstart <= cstart <= pend:
                if cend <= pend:
                    ans.append([cstart, cend])
                else:
                    ans.append([cstart, pend])
            if cend >= pend:
                prev = i
        return ans