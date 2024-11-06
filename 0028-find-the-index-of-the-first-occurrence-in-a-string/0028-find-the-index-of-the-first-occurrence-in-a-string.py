class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        
        if m < n:
            return -1

        sidx = ord('a') - 1
        P, M = 29, 10**9 + 7
        pmax = 1
        phash = rhash = 0
        for i in range(n):
            if i > 0:
                pmax = pmax * P
            
            phash = (phash * P + ord(needle[i]) - sidx) % M
            rhash = (rhash * P + ord(haystack[i]) - sidx) % M
        
        if phash == rhash:
            return 0
        
        for i in range(n, m):
            rhash = ((rhash - pmax * (ord(haystack[i - n]) - sidx)) * P + ord(haystack[i]) - sidx) % M

            if phash == rhash:
                return i - n + 1
        
        return -1