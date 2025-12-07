class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odds = (high - low) // 2
        return odds + 1 if low & 1 and high & 1 else odds