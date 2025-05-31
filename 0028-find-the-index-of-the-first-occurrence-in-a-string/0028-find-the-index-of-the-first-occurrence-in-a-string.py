class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        MOD = 10**9 + 7
        P = 29

        m, n = len(haystack), len(needle)

        if n == 0 or n > m:
            return -1

        h = 1
        thash = 0
        phash = 0
        for i in range(n):
            if i > 0:
                h = h * P % MOD
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
                thash -= h * ord(haystack[i - n])
                thash %= MOD

                if thash < 0:
                    thash += MOD
                    
                thash *= P
                thash += ord(haystack[i])
                thash %= MOD

                if thash < 0:
                    thash += MOD
        return -1
