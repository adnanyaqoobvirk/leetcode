class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def helper(pos: int, remaining: int) -> int:
            if remaining == 0:
                return 1
            
            if pos >= n or remaining < 0:
                return 0
            
            return helper(pos, remaining - coins[pos]) + helper(pos + 1, remaining)
        n = len(coins)
        return helper(0, amount)