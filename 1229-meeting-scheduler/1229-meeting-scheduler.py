class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        
        m, n = len(slots1), len(slots2)
        
        p1 = p2 = 0
        while p1 < m and p2 < n:
            start = max(slots1[p1][0], slots2[p2][0])
            end = min(slots1[p1][1], slots2[p2][1])
            if end - start >= duration:
                return [start, start + duration]
            elif slots1[p1][1] < slots2[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return []