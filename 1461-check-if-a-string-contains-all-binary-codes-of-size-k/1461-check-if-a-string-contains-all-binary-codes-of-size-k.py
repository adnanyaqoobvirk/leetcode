class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        MAX_SET_SIZE = 1 << k
        BIT_MASK = MAX_SET_SIZE - 1
        
        code = int(s[0:k], 2)
        codes = {code}
        for i in range(k, len(s)):
            code = (code << 1) & BIT_MASK | int(s[i])
            codes.add(code)
        return len(codes) == MAX_SET_SIZE