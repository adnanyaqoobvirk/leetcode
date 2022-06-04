class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def helper(pos: int) -> int:
            if pos == n:
                return 1
            
            return (
                helper(pos + 1) if s[pos] != '0' else 0
            ) + (
                helper(pos + 2) if pos < n - 1 and 10 <= int(f"{s[pos]}{s[pos + 1]}") <= 26 else 0
            )
        n = len(s)
        return helper(0)