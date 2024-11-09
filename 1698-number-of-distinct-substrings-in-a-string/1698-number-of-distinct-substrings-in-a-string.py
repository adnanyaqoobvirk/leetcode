class Solution:
    def countDistinct(self, s: str) -> int:
        P, M = 127, 2**40 + 2**8 + 0xb3
        h = ans = 0
        pmax = 1
        for i in range(len(s)):
            h = (h * P + ord(s[i])) % M
            r, seen = h, {h}
            for j in range(i + 1, len(s)):
                r -= pmax * ord(s[j - i - 1])
                r = (r * P + ord(s[j])) % M
                seen.add(r)
            ans += len(seen)
            pmax = pmax * P % M
        return ans