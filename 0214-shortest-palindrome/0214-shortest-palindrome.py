class Solution:
    def shortestPalindrome(self, s: str) -> str:
        P, M = 127, 2**40 + 2**8 + 0xb3
        
        n = len(s)
        lhashes, pmaxes = [], []
        lhash = rhash = 0
        pmax = 1
        for i in range(n):
            lhash = (lhash * P + ord(s[i])) % M
            lhashes.append(lhash)

            rhash = (rhash * P + ord(s[n - i - 1])) % M
            
            pmax = pmax * P % M
            pmaxes.append(pmax)

        if lhash == rhash:
            return s
        
        for i in reversed(range(1, n)):
            rhash -= pmaxes[i - 1] * ord(s[i])
            rhash %= M
            if lhashes[i - 1] == rhash:
                return s[i:][::-1] + s
        return s[1:][::-1] + s