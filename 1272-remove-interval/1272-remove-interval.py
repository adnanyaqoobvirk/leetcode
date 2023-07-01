class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        rstart, rend = toBeRemoved
        ans = []
        for start, end in intervals:
            if start >= rend or end <= rstart:
                ans.append([start, end])
                continue
                
            if start < rstart:
                ans.append([start, rstart])
            
            if end > rend:
                ans.append([rend, end])
        return ans