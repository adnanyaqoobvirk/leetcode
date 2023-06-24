class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        
        if abs(n - m) > 1:
            return False
        
        if n == m:
            edits = 0
            for i in range(n):
                if s[i] != t[i]:
                    edits += 1
            return edits == 1
        elif n > m:
            s, t = t, s
            n, m = m, n
            
        i = 0
        for c in t:
            if i < n and c == s[i]:
                i += 1
        return i == n
