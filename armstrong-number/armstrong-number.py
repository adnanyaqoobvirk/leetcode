class Solution:
    def isArmstrong(self, n: int) -> bool:
        k = math.floor(math.log(n, 10)) + 1
        m = n
        total = 0
        while m > 0:
            m, d = divmod(m, 10)
            total += d ** k
        return total == n