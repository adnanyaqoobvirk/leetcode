class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)

        if n == 0:
            return 0
        
        if n > m:
            return -1
        
        MOD = 10**9 + 7
        P = 29

        h = (P ** (n - 1)) % MOD
        thash = phash = 0
        for i in range(n):
            thash = (thash * P + ord(haystack[i])) % MOD
            phash = (phash * P + ord(needle[i])) % MOD
        
        for i in range(n, m + 1):
            if thash == phash:
                for j in range(n):
                    if haystack[i - n + j] != needle[j]:
                        break
                else:
                    return i - n
            
            if i < m:
                thash = (thash - h * ord(haystack[i - n])) % MOD
                thash = (thash * P + ord(haystack[i])) % MOD
        return -1
