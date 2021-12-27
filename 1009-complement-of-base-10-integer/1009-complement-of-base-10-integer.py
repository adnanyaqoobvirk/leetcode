class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        bitmask = n
        bitmask |= bitmask >> 1
        bitmask |= bitmask >> 2
        bitmask |= bitmask >> 4
        bitmask |= bitmask >> 8
        bitmask |= bitmask >> 16
        return n ^ bitmask