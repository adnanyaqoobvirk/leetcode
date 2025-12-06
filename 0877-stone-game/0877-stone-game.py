class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        def dp(i: int, j: int) -> int:
            if i == j:
                return 0
            
            return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
        n = len(piles)
        total_half = sum(piles) // 2
        return dp(0, n - 1) > total_half