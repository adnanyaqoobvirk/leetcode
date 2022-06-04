class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos == n:
                return 1
            
            count = 0
            if s[pos] != '0':
                count += helper(pos + 1)
            
            if pos < n - 1 and 10 <= int(f"{s[pos]}{s[pos + 1]}") <= 26:
                count += helper(pos + 2)
            return count
        n = len(s)
        return helper(0)