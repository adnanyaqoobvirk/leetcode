class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        
        i = 0
        for c in s:
            while i < n and t[i] != c:
                i += 1
            if i == n:
                return False
            i += 1
        return True