class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        lo, hi = 0, int(sqrt(c))
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            res = lo * lo + hi * hi
            if res == c:
                return True
            elif res > c:
                if lo * lo + mid * mid <= c:
                    hi = hi - 1
                else:
                    hi = mid - 1
            else:
                if hi * hi + mid * mid >= c:
                    lo = lo + 1
                else:
                    lo = mid + 1
        return False