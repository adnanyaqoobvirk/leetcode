class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        def gcd(x: int, y: int) -> int:
            while y > 0:
                x, y = y, x % y
            return x
        
        def lcm(x: int, y: int) -> int:
            return x * y // gcd(x, y)
        
        def magicalNumbers(x: int) -> int:
            return x // a + x // b - x // l
        
        lo, hi, l = min(a, b), n * min(a, b), lcm(a, b)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if magicalNumbers(mid) < n:
                lo = mid + 1
            else:
                hi = mid
        return lo % (10**9 + 7)