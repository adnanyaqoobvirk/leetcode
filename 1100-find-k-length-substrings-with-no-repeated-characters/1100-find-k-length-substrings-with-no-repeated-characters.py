class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        scount = l = 0
        chars = set()
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
                
            chars.add(s[r])
            
            if len(chars) >= k:
                scount += 1
                chars.remove(s[l])
                l += 1
        return scount