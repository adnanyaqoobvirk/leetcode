class Solution:
    def isArmstrong(self, n: int) -> bool:
        digits = []
        m = n
        while m > 0:
            digits.append(m % 10)
            m //= 10
        
        k = len(digits)
        total = 0
        for d in digits:
            total += d ** len(digits)
        return total == n