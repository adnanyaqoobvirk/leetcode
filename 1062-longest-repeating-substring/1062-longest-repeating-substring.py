class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        def valid(l: int) -> bool:
            P, M = 127, 10**9 + 7

            rhash, pmax = 0, 1
            for i in range(l):
                if i > 0:
                    pmax = pmax * P % M
                rhash = (rhash * P + ord(s[i])) % M
            
            seen = {rhash}
            for i in range(l, n):
                rhash -= pmax * ord(s[i - l])
                rhash = (rhash * P + ord(s[i])) % M

                if rhash in seen:
                    return True
                seen.add(rhash)
            return False

        n = len(s)
        lo, hi = 0, len(s)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if valid(mid):
                lo = mid
            else:
                hi = mid
        return lo
