class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def valid(minutes: int) -> bool:
            extra = 0
            for p in batteries:
                extra += min(p, minutes)
            return extra // n >= minutes
        
        l, h = 0, sum(batteries) + 1
        while l + 1 < h:
            m = l + h >> 1
            if valid(m):
                l = m
            else:
                h = m
        return l