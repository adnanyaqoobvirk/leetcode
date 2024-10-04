class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
            
        mask = 2 ** k - 1
        seen = set(i for i in range(mask + 1))
        num = 0
        for i in range(k):
            num = num << 1
            num |= int(s[i])
        
        if num in seen:
            seen.remove(num)
        
        for i in range(k, len(s)):
            num = num << 1
            num |= int(s[i])
            num &= mask

            if num in seen:
                seen.remove(num)
        
        return not seen