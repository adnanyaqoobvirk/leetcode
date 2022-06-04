class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        prev, curr = 0, 1
        for pos in reversed(range(n)):
            count = 0
            if s[pos] != '0':
                count += curr
            
            if pos < n - 1 and 10 <= int(f"{s[pos]}{s[pos + 1]}") <= 26:
                count += prev
            prev, curr = curr, count
        return curr