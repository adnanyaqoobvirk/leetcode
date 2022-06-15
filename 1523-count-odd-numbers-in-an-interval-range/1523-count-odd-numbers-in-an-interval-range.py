class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total = (high - low + 1) // 2
        return total + 1 if low & 1 and high & 1 else total