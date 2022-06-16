class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        total = 0
        while n > 0:
            n, d = divmod(n, 10)
            product *= d
            total += d
        return product - total