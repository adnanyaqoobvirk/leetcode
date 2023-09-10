class Solution:
    def countOrders(self, n: int) -> int:
        @cache
        def helper(p: int, d: int) -> int:
            if p < 0 or d < 0:
                return 0
            
            if p == 0 and d == 0:
                return 1
            elif p == 0:
                return math.factorial(d)
            
            if d < p:
                return 0
            
            return p * helper(p - 1, d) + (d - p) * helper(p, d - 1)
        return helper(n, n) % (10 ** 9 + 7)