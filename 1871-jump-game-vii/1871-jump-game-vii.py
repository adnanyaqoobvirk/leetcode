class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        @cache
        def dp(i: int) -> bool:
            if i == n - 1:
                return True
            
            l = i + minJump
            r = min(i + maxJump, n - 1)
            while l <= r:
                if s[l] == '0' and dp(l):
                    return True
                l += 1
            
            return False
        n = len(s)
        return dp(0)