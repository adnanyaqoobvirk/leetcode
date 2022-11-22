class Solution:
    def mySqrt(self, x: int) -> int:
        lo, hi = 0, x + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid
        return lo