class Solution:
    def minOperations(self, n: int) -> int: 
        if n == 0:
            return 0

        bl = n.bit_length()
        return 1 + self.minOperations(min((1 << bl) - n, n - (1 << bl - 1)))
