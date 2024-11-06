class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        
        if m < n:
            return -1

        P, M = 127, 10**9 + 7
        pmax = 1
        phash = rhash = 0
        for i in range(n):
            if i > 0:
                pmax = pmax * P
            
            phash = (phash * P + ord(needle[i])) % M
            rhash = (rhash * P + ord(haystack[i])) % M
        
        if phash == rhash:
            return 0
        
        for i in range(n, m):
            rhash = ((rhash - pmax * ord(haystack[i - n])) * P + ord(haystack[i])) % M

            if phash == rhash:
                return i
        
        return -1