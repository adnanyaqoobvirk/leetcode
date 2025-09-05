class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 60):
            x = num1 - k * num2
            if x < k:
                break
            if k >= x.bit_count():
                return k
        return -1