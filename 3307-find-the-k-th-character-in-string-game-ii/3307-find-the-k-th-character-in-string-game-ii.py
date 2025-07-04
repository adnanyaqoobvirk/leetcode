class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        mid = k
        bl = k.bit_length()
        if k & (k - 1) != 0:
            mid = 1 << bl
        
        ops = 0
        for i in reversed(range(bl)):
            mid >>= 1
            if k > mid and operations[i] == 1:
                ops += 1
                k = k - mid
        return chr(ord("a") + (ops % 26))