class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False

        return bool(n & n - 1 == 0 and n.bit_length() & 1)