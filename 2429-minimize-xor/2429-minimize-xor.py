class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bcount = num2.bit_count() - num1.bit_count()
        x = num1
        if bcount < 0:
            for _ in range(-bcount):
                x &= ~(x & -x)
        else:
            for _ in range(bcount):
                j = 0
                while (x & (1 << j)) != 0:
                    j += 1
                x |= (1 << j)
        return x