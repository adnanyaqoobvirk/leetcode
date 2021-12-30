class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if not (k & 1):
            return -1
        
        r = 1
        for nsize in range(1, k + 1):
            r %= k
            if r == 0:
                return nsize
            r = r * 10 + 1
        return -1