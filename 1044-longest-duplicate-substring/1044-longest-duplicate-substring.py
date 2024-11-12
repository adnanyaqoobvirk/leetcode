class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def getIndex(l: int) -> int:
            rhash = 0
            pmax = 1
            for i in range(l):
                rhash = (rhash * P + ord(s[i])) % M
                if i > 0:
                    pmax = pmax * P % M
            
            seen = {rhash}
            for i in range(l, n):
                rhash -= pmax * ord(s[i - l])
                rhash = (rhash * P + ord(s[i])) % M

                if rhash in seen:
                    return i - l + 1
                seen.add(rhash)
            return -1

        P, M = 127, 2**40 + 2**8 + 0xb3
        n = len(s)
        lo, hi = 0, n
        idx = -1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            i = getIndex(mid)
            if i > -1:
                lo = mid
                idx = i
            else:
                hi = mid
        return "" if lo == 0 else s[idx:idx + lo]