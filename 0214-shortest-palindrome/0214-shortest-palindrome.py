class Solution:
    def shortestPalindrome(self, s: str) -> str:
        P, M = 127, 2**40 + 2**8 + 0xb3
        n = len(s)
        lhash = rhash = r = 0
        pmax = 1
        for i in range(n):
            lhash = (lhash * P + ord(s[i])) % M
            rhash = (rhash + ord(s[i]) * pmax) % M
            pmax = pmax * P % M
            if lhash == rhash:
                r = i
        return s[r + 1:][::-1] + s