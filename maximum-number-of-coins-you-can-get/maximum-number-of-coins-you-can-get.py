class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        total = 0
        for i in range(1, n // 3 + 1):
            total += piles[n - 2 * i]
        return total