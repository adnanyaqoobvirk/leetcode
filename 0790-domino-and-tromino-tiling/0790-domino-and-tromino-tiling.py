class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def dp(m: int, t: bool = False) -> int:
            if m == 0 and not t:
                return 1

            if m < 0:
                return 0
            
            if t:
                return (dp(m - 1, True) + dp(m - 1)) % MOD
            else:
                return (dp(m - 1) + dp(m - 2) + 2 * dp(m - 2, True)) % MOD
        MOD = 10**9 + 7
        return dp(n)