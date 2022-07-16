class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, h = len(needle), len(haystack)
        if n > h:
            return -1
        
        MAX_CHARS = 26
        
        nhash = 0
        for i, c in enumerate(needle):
            nhash += MAX_CHARS**i + ord(c)
        
        hhash = 0
        for i in range(n):
            hhash += MAX_CHARS**i + ord(haystack[i])
        
        for i in range(n, h + 1):
            k = i - n
            if hhash == nhash:
                for j in range(n):
                    if haystack[k + j] != needle[j]:
                        break
                else:
                    return k
            if i < h:
                hhash -= ord(haystack[k])
                hhash += ord(haystack[i])
        
        return -1
                