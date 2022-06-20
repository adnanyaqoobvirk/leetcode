class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n + 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            total = mid * (mid + 1) // 2
            if total > n:
                hi = mid
            else:
                lo = mid + 1
        return lo - 1