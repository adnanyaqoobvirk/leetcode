class Solution:
    def countDistinct(self, s: str) -> int:
        P, M = 127, 2**88 + 2**8 + 0x3b
        n = len(s)
        seen = set()
        for i in range(n):
            h = 0
            for j in range(i, n):
                h = (h * P + ord(s[j])) % M
                seen.add(h)
        return len(seen)