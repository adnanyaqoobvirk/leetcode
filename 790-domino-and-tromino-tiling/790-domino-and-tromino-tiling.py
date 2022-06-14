class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def helper(pos: int, domino: bool) -> int:
            if pos <= 2:
                return pos
            
            if domino:
                return (
                    helper(pos - 1, True) + 
                    helper(pos - 2, True) + 
                    2 * helper(pos - 2, False)
                ) % MOD
            else:
                return (
                    helper(pos - 1, False) +
                    helper(pos - 1, True)
                ) % MOD
        MOD = 10**9 + 7
        return helper(n, True)