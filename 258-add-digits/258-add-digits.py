class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n = num
            total = 0
            while n > 0:
                n, d = divmod(n, 10)
                total += d
            num = total
        return num