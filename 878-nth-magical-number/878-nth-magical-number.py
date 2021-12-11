class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        lo, hi, l = min(a, b), n * min(a, b), a * b // gcd(a, b)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if mid // a + mid // b - mid // l < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % (10**9 + 7)