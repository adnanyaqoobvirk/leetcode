class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def helper(f: int) -> int:
            if f == 1:
                return k
            elif f == 2:
                return k * k
        
            return (k - 1) * (helper(f - 1) + helper(f - 2))
        return helper(n)