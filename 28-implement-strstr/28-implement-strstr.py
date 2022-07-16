class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(needle), len(haystack)
        
        if n > m:
            return -1
        
        for i in range(m):
            for j in range(n):
                if i + j < m and needle[j] == haystack[i + j]:
                    continue
                else:
                    break
            else:
                return i
        return -1