class Solution:
    def kthCharacter(self, k: int) -> str:
        mid = k
        if k & (k - 1) != 0:
            mid = 1 << k.bit_length()
        
        ops = 0
        while mid > 1:
            mid >>= 1
            if k > mid:
                ops += 1
                k = k - mid
        return chr(ord("a") + (ops % 26))