class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        def possible(l: int) -> bool:
            common = None
            for p in paths:
                if l > len(p):
                    return False
                ncommon = set()
                rhash = 0
                pmax = 1
                for i in range(l):
                    rhash = (rhash * P + p[i]) % M
                    if i > 0:
                        pmax = pmax * P % M

                if not common or rhash in common:
                    ncommon.add(rhash)

                for i in range(l, len(p)):
                    rhash -= pmax * p[i - l]
                    rhash = (rhash * P + p[i]) % M

                    if not common or rhash in common:
                        ncommon.add(rhash)
                
                if len(ncommon) == 0:
                    return False

                common = ncommon
            return True                

        P, M = 10**5 + 1, 2**88 + 2**8 + 0x3b
        lo, hi = 0, max(len(p) for p in paths) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            if possible(mid):
                lo = mid
            else:
                hi = mid
        return lo