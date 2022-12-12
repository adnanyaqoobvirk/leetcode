class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def helper(pos):
            if pos > n:
                return 0
            
            if pos == n:
                return 1
            
            return helper(pos + 1) + helper(pos + 2)
        return helper(0)