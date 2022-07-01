class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def helper(m: int) -> int:
            if m == 0:
                return 1
            
            if m <= 2:
                return m
            
            ans = 0
            for i in range(1, m + 1):
                ans += helper(i - 1) * helper(m - i)
                
            return ans
        return helper(n)
    
        