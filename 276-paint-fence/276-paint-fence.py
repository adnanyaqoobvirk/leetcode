class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos == 1:
                return k
            
            if pos == 2:
                return k * k
            
            return (k - 1) * (helper(pos - 1) + helper(pos - 2))
        return helper(n)