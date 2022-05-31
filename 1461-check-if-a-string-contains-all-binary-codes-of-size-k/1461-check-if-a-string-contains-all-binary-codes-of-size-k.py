class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MAX_SET_SIZE = 1 << k
        BIT_MASK = MAX_SET_SIZE - 1
        
        codes = [False] * MAX_SET_SIZE
        code = int(s[0:k], 2)
        codes[code] = True
        for i in range(k, len(s)):
            code = (code << 1) & BIT_MASK | int(s[i])
            codes[code] = True
        return all(codes)