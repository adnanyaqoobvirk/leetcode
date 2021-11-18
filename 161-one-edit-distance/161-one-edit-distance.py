class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) - len(t) > 1:
            return False
        
        if len(t) > len(s):
            s, t = t, s
        
        n, m = len(s), len(t)
        for i in range(m):
            if s[i] != t[i]:
                if n == m:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i + 1:] == t[i:]
        return m + 1 == n
                