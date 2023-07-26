class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def valid(v: int) -> bool:
            c = 0
            for d in dist:
                c = math.ceil(c)
                c += d / v
            return c <= hour
        
        l, r = 0, sum(dist) * 10 * 10
        while l + 1 < r:
            m = l + r >> 1
            if valid(m):
                r = m
            else:
                l = m
        return r if valid(r) else -1