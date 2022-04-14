class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            mid_double = mid * mid
            if mid_double == num:
                return True
            elif mid_double > num:
                hi = mid - 1
            else:
                lo = mid + 1
        return False