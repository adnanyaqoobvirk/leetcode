class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        res = 0
        mask = 1
        while mask <= n:
            if n & mask == 0:
                res |= mask
            mask <<= 1
        return res