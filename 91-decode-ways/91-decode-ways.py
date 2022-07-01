class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos >= n:
                return 1
            
            if s[pos] == '0':
                return 0
            
            ans = helper(pos + 1)
            
            if pos < n - 1:
                if s[pos] == '1' or (s[pos] == '2' and int(s[pos + 1]) <= 6):
                    ans += helper(pos + 2)
            
            return ans
        
        n = len(s)
        return helper(0)