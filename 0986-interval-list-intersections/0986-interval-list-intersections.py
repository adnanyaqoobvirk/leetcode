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
            if firstList[p1][1] <= secondList[p2][1]:
                if firstList[p1][0] >= secondList[p2][0]:
                    ans.append(firstList[p1])
                else:
                    if secondList[p2][0] <= firstList[p1][1]:
                        ans.append([secondList[p2][0], firstList[p1][1]])
                p1 += 1
            else:
                if secondList[p2][0] >= firstList[p1][0]:
                    ans.append(secondList[p2])
                else:
                    if firstList[p1][0] <= secondList[p2][1]:
                        ans.append([firstList[p1][0], secondList[p2][1]])
                p2 += 1
        return ans