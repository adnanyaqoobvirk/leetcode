class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) - len(t) > 1:
            return False
        
        if len(t) > len(s):
            s, t = t, s
        
        n, m = len(s), len(t)
        i = j = diff = 0
        while i < n and diff <= 1:
            if j < m:
                if s[i] == t[j]:
                    j += 1
                else:
                    diff += 1
                    if n == m:
                        j += 1
            else:
                diff += 1
            i += 1
        return diff == 1