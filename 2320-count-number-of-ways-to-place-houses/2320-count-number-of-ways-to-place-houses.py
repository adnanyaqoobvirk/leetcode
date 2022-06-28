class Solution:
    def countHousePlacements(self, n: int) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos >= n:
                return 1
            
            return (helper(pos + 1) + helper(pos + 2)) % MOD
        MOD = 10**9 + 7
        return helper(0)**2 % MOD
    
        