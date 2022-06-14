class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def domino(pos: int) -> int:
            if pos <= 2:
                return pos
            
            return (domino(pos - 1) + domino(pos - 2) + 2 * tromino(pos - 2)) % MOD
        
        @cache
        def tromino(pos: int) -> int:
            if pos <= 2:
                return pos
            
            return (tromino(pos - 1) + domino(pos - 1)) % MOD
        MOD = 10**9+7
        return domino(n)