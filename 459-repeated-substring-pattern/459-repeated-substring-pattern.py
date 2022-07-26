class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        MAX_CHARS = 26
        MOD = 900001
        
        ss = (s + s)[1:-1]
        
        if not ss:
            return False
        
        n, m = len(s), len(ss)
        
        h = 1
        for i in range(n - 1):
            h = (MAX_CHARS * h) % MOD
        
        shash = sshash = 0
        for i in range(n):
            shash = (MAX_CHARS * shash + ord(s[i])) % MOD
            sshash = (MAX_CHARS * sshash + ord(ss[i])) % MOD
        
        for i in range(n, m + 1):
            k = i - n
            if shash == sshash:
                for j in range(n):
                    if s[j] != ss[j + k]:
                        break
                else:
                    return True
            
            if i < m:
                sshash = (MAX_CHARS * (sshash - h * ord(ss[k])) + ord(ss[i])) % MOD
                
                if sshash < 0:
                    sshash += MOD
        return False