class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        
        prev = curr = 1
        for pos in reversed(range(n)):
            if s[pos] == '0':
                prev, curr = curr, 0
                continue
                
            ans = curr
            if pos < n - 1:
                if s[pos] == '1' or (s[pos] == '2' and int(s[pos + 1]) <= 6):
                    ans += prev
            prev, curr = curr, ans
        return curr