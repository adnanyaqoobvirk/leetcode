class Solution:
    def shortestPalindrome(self, s: str) -> str:
        P, M = 127, 2**24 + 2**8 + 0x93
        n = len(s)
        lhash = rhash = r = 0
        pmax = 1
        for i in range(n):
            lhash = (lhash * P + ord(s[i])) % M
            rhash = (rhash + ord(s[i]) * pmax) % M
            pmax = pmax * P % M
            if lhash == rhash:
                ps = s[:i + 1]
                if ps == ps[::-1]:
                    r = i
        return s[r + 1:][::-1] + s