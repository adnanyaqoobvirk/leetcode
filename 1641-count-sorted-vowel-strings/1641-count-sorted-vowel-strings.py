class Solution:
    def countVowelStrings(self, n: int) -> int:
        @cache
        def helper(pos: int, count: int) -> int:
            if pos >= 5:
                return 0
            
            if count == n:
                return 1
            
            ans = 0
            for i in range(pos, 5):
                ans += helper(i, count + 1)
            return ans
        return helper(0, 0)