class Solution:
    def totalMoney(self, n: int) -> int:
        d, r = divmod(n, 7)
        return (7 * d * (7 + d) + r * (2 * d + 1 + r)) // 2
        