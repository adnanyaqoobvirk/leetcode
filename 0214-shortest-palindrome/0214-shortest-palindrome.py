class Solution:
    def shortestPalindrome(self, s: str) -> str:
        P1, M1 = 31, 2**24 + 2**8 + 0x93
        P2, M2 = 29, 10**9 + 7
        lhash1 = rhash1 = lhash2 = rhash2 = r = 0
        pmax1 = pmax2 = 1
        for i in range(len(s)):
            lhash1 = (lhash1 * P1 + ord(s[i]) - ord('a') + 1) % M1
            rhash1 = (rhash1 + (ord(s[i]) - ord('a') + 1) * pmax1) % M1
            pmax1 = pmax1 * P1 % M1

            lhash2 = (lhash2 * P2 + ord(s[i]) - ord('a') + 1) % M2
            rhash2 = (rhash2 + (ord(s[i]) - ord('a') + 1) * pmax2) % M2
            pmax2 = pmax2 * P2 % M2

            if lhash1 == rhash1 and lhash2 == rhash2:
                r = i
        return s[r + 1:][::-1] + s