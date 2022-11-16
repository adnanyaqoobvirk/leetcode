class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if (mid * (mid + 1) // 2) <= n:
                lo = mid
            else:
                hi = mid
        return lo