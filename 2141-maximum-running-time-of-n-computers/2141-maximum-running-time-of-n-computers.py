class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l, h = 0, sum(batteries) // n + 1
        while l + 1 < h:
            m = l + h >> 1
            
            extra = 0
            for p in batteries:
                extra += min(p, m)
                
            if extra // n >= m:
                l = m
            else:
                h = m
        return l