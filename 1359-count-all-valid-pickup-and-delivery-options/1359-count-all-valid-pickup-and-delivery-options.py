class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        @cache
        def helper(p: int, d: int) -> int:
            if p < 0 or d < 0 or d < p:
                return 0
            
            if p == 0 and d == 0:
                return 1
            
            return (p * helper(p - 1, d)) % MOD + ((d - p) * helper(p, d - 1)) % MOD
        return helper(n, n) % MOD