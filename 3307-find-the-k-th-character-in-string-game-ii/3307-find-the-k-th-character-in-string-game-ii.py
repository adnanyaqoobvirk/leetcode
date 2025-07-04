class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        mid = k
        bl = k.bit_length()
        if k & (k - 1) != 0:
            mid = 1 << bl
        else:
            bl -= 1
        
        ops = 0
        for i in reversed(range(bl)):
            if mid <= 1:
                break
            mid >>= 1
            if k > mid:
                if operations[i] == 1:
                    ops += 1
                k = k - mid
        return chr(ord("a") + (ops % 26))