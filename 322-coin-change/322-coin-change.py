class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(i: int, remaining: int) -> int:
            if i == n or remaining < 0:
                return inf
            
            if remaining == 0:
                return 0
            
            return min(
                1 + helper(i, remaining - coins[i]),
                helper(i + 1, remaining)
            )
        
        n = len(coins)
        ans = helper(0, amount)
        return ans if ans != inf else -1