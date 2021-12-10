class Solution:
    def numTilings(self, n: int) -> int:
        @cache
        def domino(k: int) -> int:
            if k <= 2:
                return k
            
            return domino(k - 1) + domino(k - 2) + 2 * tromino(k - 2)
        
        @cache
        def tromino(k: int) -> int:
            if k <= 2:
                return k
            
            return tromino(k - 1) + domino(k - 1)
        
        return domino(n) % (10**9 + 7)