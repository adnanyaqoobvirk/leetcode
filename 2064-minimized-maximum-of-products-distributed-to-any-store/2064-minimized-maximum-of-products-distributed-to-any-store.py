class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def possible(x: int) -> bool:
            r = n
            for q in quantities:
                c = ceil(q / x)
                if c > r:
                    return False
                r -= c
            return True
        
        lo, hi = 0, max(quantities)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if possible(mid):
                hi = mid
            else:
                lo = mid
        return hi