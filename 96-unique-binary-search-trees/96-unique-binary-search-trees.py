class Solution:
    def numTrees(self, n: int) -> int:
        def helper(left: int, right: int) -> int:
            if (left, right) in cache:
                return cache[(left, right)]
            
            if right - left <= 0:
                return 1
            
            ans = 0
            for i in range(left, right + 1):
                ans += helper(left, i - 1) * helper(i + 1, right)
            cache[(left, right)] = ans
            return ans
        
        cache = {}
        return helper(1, n)