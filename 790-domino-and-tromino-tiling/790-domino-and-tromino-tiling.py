class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1: return 1
        mod, pg, cg, pu, cu = 10**9 + 7, 1, 2, 1, 2
        for _ in range(3, n + 1):
            pg, cg, pu, cu = cg, (cg + pg + 2 * pu) % mod, cu, (cu + cg) % mod
        return cg